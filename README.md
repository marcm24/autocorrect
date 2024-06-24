# autocorrect
.txt file autocorrect application

In this program we will be implementing autocorrect to a text file that contains mispelled words.
To look for and fix the spelling errors within the file, there will be various checks to find a properly spelled word.
One of the checks we are going to test removing each of the letters from the word one by one. this will be the drop check.
The next chceck will be inserting any letter from the alphabet into all positions of the word. this is the insert check.
The next check will be swapping 2 letters next to each other at each position of the word. for example,
If the word is hello, we will swap it to ehllo first as those are the first 2 letters. next will be hlelo, and so on. this is the swap check.
The next check will be replacing each of the letters with corresponding keyboard values from the keyboard dictionary. this is the replace check.
All of the outcomes of these checks will be run through the overall dictionary to see if they are within the dictionary,
And that will be our test word list. From there, we will sort those words by their frequencies within the list, and print them out next to the words they
originated from.
