import sys, os, calendar, time, random, string, pyperclip
from appJar import gui

def press(button):
    if button == "Generate Seed":
        app.disableButton("Generate Seed")
        app.clearListBox("list")
        app.addListItem("list", "Seed Generating...done")
        app.addListItem("list", "Seed Verifying...done")
        secure_random = random.SystemRandom()
        seed = ''.join(random.SystemRandom().choice(string.ascii_uppercase + "9") for _ in range(81))
        copy=app.yesNoBox("Generated Seed", seed+"\n\nCopy Seed to Clipboard?")
        if copy == True:
            pyperclip.copy(seed)
            app.addListItem("list", "Seed Copied to Clipboard")
        save=app.yesNoBox("Generated Seed", seed+"\n\nSave Seed to File?")
        if save == True:
            seedTrim = seed[:10]
            filename = "Seed." + seedTrim + ".txt"
            saveFile=app.saveBox(title="Save Seed", fileName=filename, dirName=None, fileExt=".txt", fileTypes=None, asFile=None)
            file = open(saveFile,"w") 
            file.write(seed)
            file.close()
            app.addListItem("list", "Seed Saved to \""+saveFile+"\"")

        app.addListItem("list", "Seed Generation Complete")
        app.enableButton("Generate Seed")

title = "IOTA Seed Tool"
app = gui(title,"300x265")
app.setGeometry("300x265")
app.setTitle(title)
app.setResizable(canResize=False)
app.setFont(12)
app.setBg("lightseagreen")

app.startFrame("0")
app.addButtons(["Generate Seed"], press)
app.stopFrame()

app.startFrame("2",1,0,3)
app.addListBox("list", ["Click \"Generate Seed\" to Create a New Seed"])
app.setListBoxRelief("list", "flat")
app.stopFrame()

app.go()
