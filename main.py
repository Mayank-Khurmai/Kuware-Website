import os

## Number of days you want to make commits
for i in range(10,15):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('temp.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add temp.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

os.system('git push -f')
