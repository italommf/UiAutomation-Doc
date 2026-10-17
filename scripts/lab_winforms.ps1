# Laboratório próprio para testar o uiautomation (janela "UIA-LAB"), com AutomationId em tudo.
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$f = New-Object Windows.Forms.Form
$f.Text = "UIA-LAB"; $f.Name = "frmLab"; $f.Width = 1000; $f.Height = 800; $f.StartPosition = "Manual"; $f.Left = 100; $f.Top = 60
function Add($c,$name,$x,$y,$w,$h,$text){ $c.Name=$name; $c.Left=$x;$c.Top=$y;$c.Width=$w;$c.Height=$h; if($text){$c.Text=$text}; $f.Controls.Add($c); $c }
$lbl = Add (New-Object Windows.Forms.Label) "lblStatus" 10 5 400 20 "evento: nenhum"
$script:n = 0
$btn = Add (New-Object Windows.Forms.Button) "btnClick" 10 30 120 28 "Clicar"
$btn.Add_Click({ $script:n++; $lbl.Text = "evento: clique $script:n" })
$btnD = Add (New-Object Windows.Forms.Button) "btnDesab" 140 30 120 28 "Desabilitado"; $btnD.Enabled = $false
$chk = Add (New-Object Windows.Forms.CheckBox) "chkAceito" 10 65 150 24 "Aceito os termos"
$chk.Add_CheckedChanged({ $lbl.Text = "evento: chk=" + $chk.Checked })
$chk3 = Add (New-Object Windows.Forms.CheckBox) "chkTri" 170 65 150 24 "Tri-estado"; $chk3.ThreeState = $true
$r1 = Add (New-Object Windows.Forms.RadioButton) "rdA" 10 95 80 24 "Opção A"
$r2 = Add (New-Object Windows.Forms.RadioButton) "rdB" 100 95 80 24 "Opção B"
$r1.Add_CheckedChanged({ if($r1.Checked){$lbl.Text="evento: radio A"} }); $r2.Add_CheckedChanged({ if($r2.Checked){$lbl.Text="evento: radio B"} })
$cmb = Add (New-Object Windows.Forms.ComboBox) "cmbCor" 10 125 150 24 ""; $cmb.DropDownStyle="DropDownList"; [void]$cmb.Items.AddRange(@("Vermelho","Verde","Azul","Amarelo"))
$cmb.Add_SelectedIndexChanged({ $lbl.Text = "evento: cor=" + $cmb.SelectedItem })
$cmbE = Add (New-Object Windows.Forms.ComboBox) "cmbEditavel" 170 125 150 24 ""; [void]$cmbE.Items.AddRange(@("um","dois","tres"))
$txt = Add (New-Object Windows.Forms.TextBox) "txtNome" 10 155 200 24 ""
$txt.Add_TextChanged({ $lbl.Text = "evento: texto=" + $txt.Text })
$pwd = Add (New-Object Windows.Forms.TextBox) "txtSenha" 220 155 150 24 ""; $pwd.UseSystemPasswordChar = $true
$ml = Add (New-Object Windows.Forms.TextBox) "txtMulti" 10 185 360 80 "linha 1`r`nlinha 2`r`nlinha 3 com acentuação: çãõé"; $ml.Multiline=$true; $ml.ScrollBars="Vertical"
$lb = Add (New-Object Windows.Forms.ListBox) "lstItens" 380 30 150 100 ""; [void]$lb.Items.AddRange(@("Item 1","Item 2","Item 3","Item 4")); $lb.SelectionMode="MultiExtended"
$lv = Add (New-Object Windows.Forms.ListView) "lvTabela" 540 30 430 100 ""; $lv.View="Details"; $lv.FullRowSelect=$true; $lv.CheckBoxes=$true
[void]$lv.Columns.Add("Nome",120); [void]$lv.Columns.Add("Qtd",60); [void]$lv.Columns.Add("Preço",80)
foreach($r in @(@("Maçã","3","1,50"),@("Banana","12","0,80"),@("Uva","1","7,00"))){ $i=New-Object Windows.Forms.ListViewItem($r[0]); [void]$i.SubItems.Add($r[1]); [void]$i.SubItems.Add($r[2]); [void]$lv.Items.Add($i) }
$tv = Add (New-Object Windows.Forms.TreeView) "tvArvore" 380 140 200 125 ""
$a=$tv.Nodes.Add("Raiz A"); [void]$a.Nodes.Add("Filho A1"); [void]$a.Nodes.Add("Filho A2"); $b=$tv.Nodes.Add("Raiz B"); $b.Nodes.Add("Filho B1").Nodes.Add("Neto B1a") | Out-Null
$tb = Add (New-Object Windows.Forms.TrackBar) "trkVolume" 590 140 200 40 ""; $tb.Minimum=0; $tb.Maximum=100; $tb.Value=30
$pb = Add (New-Object Windows.Forms.ProgressBar) "pbProgresso" 590 185 200 20 ""; $pb.Value=45
$nud = Add (New-Object Windows.Forms.NumericUpDown) "nudQtd" 800 140 80 24 ""; $nud.Minimum=0;$nud.Maximum=50;$nud.Value=5
$dt = Add (New-Object Windows.Forms.DateTimePicker) "dtpData" 590 215 200 24 ""
$mc = Add (New-Object Windows.Forms.MonthCalendar) "calMes" 800 175 230 160 ""
$tabs = Add (New-Object Windows.Forms.TabControl) "tabGeral" 10 275 360 120 ""
$tp1 = New-Object Windows.Forms.TabPage; $tp1.Text="Aba Um"; $tp1.Name="tpUm"; $tp2 = New-Object Windows.Forms.TabPage; $tp2.Text="Aba Dois"; $tp2.Name="tpDois"
$inner = New-Object Windows.Forms.Button; $inner.Text="Botão na Aba Dois"; $inner.Name="btnAbaDois"; $inner.Width=140; $inner.Left=10; $inner.Top=10; $tp2.Controls.Add($inner)
$tabs.TabPages.Add($tp1); $tabs.TabPages.Add($tp2)
$gb = Add (New-Object Windows.Forms.GroupBox) "grpCaixa" 380 275 200 120 "Grupo"
$inG = New-Object Windows.Forms.CheckBox; $inG.Text="Dentro do grupo"; $inG.Name="chkGrupo"; $inG.Left=10;$inG.Top=25;$inG.Width=150; $gb.Controls.Add($inG)
$lnk = Add (New-Object Windows.Forms.LinkLabel) "lnkSite" 590 250 200 20 "Link clicável"
$lnk.Add_LinkClicked({ $lbl.Text = "evento: link" })
$dg = Add (New-Object Windows.Forms.DataGridView) "dgvDados" 10 405 560 150 ""; $dg.AllowUserToAddRows=$false
[void]$dg.Columns.Add("c1","Produto"); [void]$dg.Columns.Add("c2","Estoque"); [void]$dg.Columns.Add("c3","Preço")
[void]$dg.Rows.Add("Caneta","100","2,50"); [void]$dg.Rows.Add("Caderno","40","18,90"); [void]$dg.Rows.Add("Mochila","8","149,00")
$pic = Add (New-Object Windows.Forms.PictureBox) "picImg" 590 345 120 80 ""; $pic.BackColor=[Drawing.Color]::Tomato
$ms = New-Object Windows.Forms.MenuStrip; $ms.Name="menuPrincipal"
$mArq = New-Object Windows.Forms.ToolStripMenuItem("Arquivo"); $mArq.Name="mnuArquivo"
$mNovo = New-Object Windows.Forms.ToolStripMenuItem("Novo"); $mNovo.Name="mnuNovo"; $mNovo.Add_Click({ $lbl.Text="evento: menu Novo" })
$mSair = New-Object Windows.Forms.ToolStripMenuItem("Sair do lab"); $mSair.Name="mnuSair"; $mSair.Add_Click({ $f.Close() })
[void]$mArq.DropDownItems.Add($mNovo); [void]$mArq.DropDownItems.Add($mSair); [void]$ms.Items.Add($mArq); $f.MainMenuStrip=$ms; $f.Controls.Add($ms)
$ss = New-Object Windows.Forms.StatusStrip; $ss.Name="statusBar"; [void]$ss.Items.Add("Pronto - barra de status"); $f.Controls.Add($ss)
$ts = New-Object Windows.Forms.ToolStrip; $ts.Name="toolBar"; $tbtn=$ts.Items.Add("BotaoTool"); $tbtn.Name="tsbTool"; $tbtn.Add_Click({ $lbl.Text="evento: toolbar" }); $f.Controls.Add($ts)
$f.Add_Shown({ $f.Activate() })
[void]$f.ShowDialog()
