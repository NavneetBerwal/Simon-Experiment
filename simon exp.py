from psychopy import visual, core, event, gui
import csv, random, os

exp_info = {'Participant': '', 'Session': '1'}
dlg = gui.DlgFromDict(dictionary=exp_info, title='Simon Experiment')
if not dlg.OK:
    core.quit()

filename = f"Simon_data_{exp_info['Participant']}_S{exp_info['Session']}.csv"
filepath = os.path.join(os.getcwd(), filename)

win = visual.Window([1920, 1200], color='black', units='pix', fullscr = True)
stim = visual.TextStim(win, text='', height=50,color ='white')
fixation = visual.TextStim(win, text='+', height=50, color ='white')

stim.text = "SIMON EXPERIMENT \n\n Task : \n A circle or square will appear at one of the two positions \n\n Press 'x' for circle and 'm' for square \n\n Press any key to begin."
stim.draw()
win.flip()
event.waitKeys()

results = []

right_pos = 200
left_pos = -200
positions = [right_pos, left_pos]
stim_types = ['circle', 'square']
n_trials = 40

#random.shuffle(n_trials)
print(n_trials)
fixation_nframe = 30
stim_nframe = 15
isi_nframe = 10

clock = core.Clock()

#Practice run 

practice = 5
stim_type = "There are few practice trials, Press any key to continue"
stim.draw()
win.flip()
event.waitKeys()

for n in range(practice):
    fixation.draw()
    stim_type = random.choice(stim_types)
    stim_pos = random.choice(positions)
    if stim_type =="circle":
        stim_shape = visual.Circle(win, radius= 50, fillColor = 'white', lineColor = 'white', pos=(stim_pos, 0))
    else:
        stim_shape = visual.Rect(win, width = 100, height = 100, fillColor ='white', lineColor = 'white', pos=(stim_pos, 0))
        
    # Present fixation
    for n in range(fixation_nframe):
            fixation.draw()
            win.flip()
    
    # Present stimulus
    for n in range(stim_nframe):
        stim_shape.draw()
        win.flip()
    
    # Clear screen (ISI)
    for n in range(isi_nframe):
        win.flip()
    
    # Ask for Response
    stim.text = "What was the shape? \n\n Press 'x' for circle and 'm' for square"
    stim.draw()
    win.flip()
    clock.reset()
    keys = event.waitKeys()
stim.text = "Good work, Lets move to the real experiment"
stim.draw()
win.flip()
event.waitKeys()

trial = 0
for n in range(n_trials):
    trial+=1
    fixation.draw()
    stim_type = random.choice(stim_types)
    stim_pos = random.choice(positions)
    if stim_type == 'circle':
        stim_shape = visual.Circle(win, radius=50, fillColor='white', lineColor='white', pos=(stim_pos,0))
    else:
        stim_shape = visual.Rect(win, width=100, height=100, fillColor='white', lineColor='white', pos=(stim_pos,0))
    
    # Present fixation
    for n in range(fixation_nframe):
            fixation.draw()
            win.flip()
    
    # Present stimulus
    for n in range(stim_nframe):
        stim_shape.draw()
        win.flip()
    
    # Clear screen (ISI)
    # for n in range(isi_nframe):
    #     win.flip()
    
    # Ask for Response
    #stim.text = "What was the shape? \n\n Press 'x' for circle and 'm' for square"
    #stim.draw()
    #win.flip()
    clock.reset()
    keys = event.waitKeys(keyList=['x', 'm'])
    rt = clock.getTime()
    
    if (keys[0] == 'x' and stim_type == 'circle') or (keys[0] == 'm' and stim_type == 'square'):
        correct = "Correct"
    else:
        correct = "Incorrect"
    
    # Store trial results
    if positions == right_pos:
        position = "Right"
    else:
        position = "Left"
    results.append({'Trial': trial, 'Stimulus': stim_type, 'stim_pos': position, 'Response': keys[0], 'Correct': correct, 'RT': rt})

stim.text = "The experiment is over. \n\n Thank you for your participation!"
stim.draw()
win.flip()
event.waitKeys()
win.close()

with open(filepath, 'w', newline='') as csvfile:
    fieldnames = ['Trial', 'Stimulus', 'Position', 'Response', 'Correct', 'RT']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in results:
        writer.writerow(data)

