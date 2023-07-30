import wx
import math

def calcular_pH(concentracao_acido, Ka):
    log_concentracao = -math.log10(concentracao_acido)
    log_Ka = -math.log10(Ka)
    pH = log_Ka + log_concentracao
    return pH

tabela_acidos = {
    "CH3COOH": {"Ka": 4.8},
    "HCN": {"pKa": 4.9e-10},
    "H2S": {"pKa": 9.1e-8},
    "HCOOH": {"Ka": 1.8e-4},
    "HF": {"Ka": 6.8e-4},
    "C6H5COOH": {"Ka": 6.3e-5},
    "C6H8O7": {"Ka": 7.5e-4},
    "C3H6O3": {"Ka": 1.4e-4},
    "C4H6O6": {"Ka": 1.0e-4},
    "C2H4O2": {"Ka": 1.8e-5},
    "H2CO3": {"Ka": 4.3e-7}
}

class pHCalculatorFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="pH Calculator", size=(400, 300))
        
        panel = wx.Panel(self)
        
        self.acid_label = wx.StaticText(panel, label="Ácido:")
        self.acid_entry = wx.TextCtrl(panel)
        
        self.concentration_label = wx.StaticText(panel, label="Concentração:")
        self.concentration_entry = wx.TextCtrl(panel)
        
        self.calculate_button = wx.Button(panel, label="Calcular pH")
        self.calculate_button.Bind(wx.EVT_BUTTON, self.on_calculate)
        
        self.result_label = wx.StaticText(panel, label="")
        
        self.acid_listbox = wx.ListBox(panel, choices=list(tabela_acidos.keys()), size=(300, 100))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.acid_label, 0, wx.ALL, 5)
        sizer.Add(self.acid_entry, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.concentration_label, 0, wx.ALL, 5)
        sizer.Add(self.concentration_entry, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.calculate_button, 0, wx.ALL, 5)
        sizer.Add(self.result_label, 0, wx.ALL, 5)
        sizer.Add(self.acid_listbox, 0, wx.ALL | wx.EXPAND, 5)
        
        panel.SetSizer(sizer)
        
    def on_calculate(self, event):
        acid = self.acid_entry.GetValue()
        concentration = float(self.concentration_entry.GetValue())

        if acid in tabela_acidos:
            Ka = tabela_acidos[acid].get("Ka") or tabela_acidos[acid].get("pKa")
            pH = calcular_pH(concentration, Ka)
            self.result_label.SetLabel("O pH do ácido {} é: {:.2f}".format(acid, pH))
        else:
            self.result_label.SetLabel("Ácido não encontrado na tabela.")

if __name__ == "__main__":
    app = wx.App(False)
    frame = pHCalculatorFrame()
    frame.Show()
    app.MainLoop()
