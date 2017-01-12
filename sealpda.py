import wolframalpha
import wikipedia
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="SealPDA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Welcome to the Two-Headed Seal Personal Assistant.  Ask your question here.")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            app_id = "27WYA8-P4V8PXAGV3"
            client = wolframalpha.Client(app_id)
            result = client.query(input)
            answer = next(result.results).text
            print answer
        except:
            # wikipedia.set_lang("en")
            input = input.split(" ")
            input = " ".join(input[2:])
            print wikipedia.summary(input, sentences=2)

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
