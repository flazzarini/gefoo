Crontab fun Decipher the following
##################################
:date: 2009-11-14 00:44
:author: Frank Lazzarini
:category: Linux
:tags: crontab, linux, bash
:slug: crontab-fun-decipher-the-following

I've been croning a lot lately, and this is one cool combination of cron
which I haven't thought was possible. In this example you see how
powerful cron can be. Defying a lot specific rules in just one line of
syntax. So let's come to it ... try to decipher the following cron line.

::

    15,45 0,12,6 20 1,2,3 0 /run/somescript.sh

Please click on the Read more link to see the solution to this little
riddle.
Wow! Now this is a pretty complex crontab entry. Let's decipher it...

- 15,45 - This means that the task will run at 15 and 45 minutes past
  the hour. But what hours and what days? Well, that's coming up.
- 0.12.6 - The task will run during the hours of 0 (midnight), 12
  (noon) and 6AM.
- 20 - The task will run on the 20th day of the month. But during what
  months?
- 1,2,3 - The task will run only during the months of January, February
  and March.
- 0 - The task will only run on a Sunday.

So, when we put all of this information together, here is what it boils
down to:

This task is going to run at 0:15, 0:45, 6:15, 6:45, 12:15 and 12:45 on
the 20th of January, February and March IF that day falls on a Sunday.
Pretty cool, huh?
