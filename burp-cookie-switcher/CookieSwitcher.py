from burp import IBurpExtender, ITab, IContextMenuFactory
from javax.swing import JPanel, JLabel, JTextField, JButton, JMenuItem, BoxLayout, Box
from java.awt import GridLayout
from java.util import ArrayList

class BurpExtender(IBurpExtender, ITab, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Cookie Switcher")

        self.adminCookie = callbacks.loadExtensionSetting("admin_cookie") or ""
        self.userCookie = callbacks.loadExtensionSetting("user_cookie") or ""

        self._panel = JPanel(GridLayout(0, 1, 5, 5))
        self._panel.add(JLabel("Admin Cookie:"))
        self.adminField = JTextField(self.adminCookie, 40)
        self._panel.add(self.adminField)

        self._panel.add(JLabel("User Cookie:"))
        self.userField = JTextField(self.userCookie, 40)
        self._panel.add(self.userField)

        saveBtn = JButton("Save", actionPerformed=self.saveSettings)
        self._panel.add(saveBtn)

        callbacks.addSuiteTab(self)
        callbacks.registerContextMenuFactory(self)

    def saveSettings(self, event):
        self.adminCookie = self.adminField.getText()
        self.userCookie = self.userField.getText()
        self._callbacks.saveExtensionSetting("admin_cookie", self.adminCookie)
        self._callbacks.saveExtensionSetting("user_cookie", self.userCookie)

    def getTabCaption(self):
        return "Cookie Switcher"

    def getUiComponent(self):
        return self._panel

    def createMenuItems(self, invocation):
        menuList = ArrayList()
        ctx = invocation.getInvocationContext()
        if ctx in (invocation.CONTEXT_MESSAGE_EDITOR_REQUEST, invocation.CONTEXT_MESSAGE_VIEWER_REQUEST):
            adminItem = JMenuItem("Switch to Admin Cookie", actionPerformed=lambda e: self.replaceCookie(invocation, self.adminCookie))
            userItem = JMenuItem("Switch to User Cookie", actionPerformed=lambda e: self.replaceCookie(invocation, self.userCookie))
            menuList.add(adminItem)
            menuList.add(userItem)
        return menuList

    def replaceCookie(self, invocation, cookieValue):
        messages = invocation.getSelectedMessages()
        if not messages:
            return
        for msg in messages:
            request = msg.getRequest()
            info = self._helpers.analyzeRequest(msg.getHttpService(), request)
            headers = list(info.getHeaders())
            bodyOffset = info.getBodyOffset()
            body = request[bodyOffset:]

            newHeaders = []
            found = False
            for h in headers:
                if h.lower().startswith("cookie:"):
                    newHeaders.append("Cookie: " + cookieValue)
                    found = True
                else:
                    newHeaders.append(h)
            if not found:
                newHeaders.append("Cookie: " + cookieValue)

            newMessage = self._helpers.buildHttpMessage(newHeaders, body)
            msg.setRequest(newMessage)
