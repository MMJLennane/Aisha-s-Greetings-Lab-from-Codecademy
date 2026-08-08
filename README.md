# Aisha-s-Greetings-Lab-from-Codecademy
And another Lab from Codecademy to make use of Python skills
Aisha's Greetings
You are a part of Aisha’s Greetings - a card printing company that prints greeting cards with a hint of personalization! You want to help Aisha create a system that generates cards based on customers’ requests.

You have been provided with two pre-filled card types:

happy_bday.txt: a card with a birthday message
thankyou_card.txt: a card file with a thank you message
Click through the files on your right and see what’s in them! If you get stuck, you can look at a sample solution of the project by looking at greetings_solutions.py - but try it out on your own first.

Let’s start printing!
Setting Up Custom Greeting Cards
1.
Aisha, the owner of Aisha’s Greetings, wants to create a program that will automatically generate pre-filled orders, using her custom greeting messages. Use your knowledge of context managers to accomplish this goal!

First, import the contextlib modules @contextmanager decorator, and create a decorated function named generic that takes in card type, sender’s name, and recipient arguments.

2.
The generic() function will serve the purpose of opening a specific generic card type (Thank you card or Birthday card) so that it can be used as the base template for a more customized card.

Inside the function create the following:

A variable to store a call of the open() built-in function that opens up a generic card type based on the card type parameter in read mode. You can assume the store will receive either a birthday card request or a thank you card request.

A variable to store a call of the open() built-in function that creates (and opens) a new card named with the following pattern: < sender_name >_generic.txt.

Use the sender name parameter from the function definition. Open the file in write mode since we will need to write a new card to the file.

3.
Now, you need to make sure the context manager correctly creates a customized card from the generic template. Inside the generic() context manager use the try clause to yield a file so that it creates the following template custom card:

Dear < receiver >
< text from the generic template card > 
Sincerely, < sender >

Copy to Clipboard

Make sure to use '\n' to create line breaks!

4.
Finally, make sure to close both files after usage!

5.
It’s time for a test run! Aisha’s Greetings just got a customer ‘Mwenda’ who requested an order for a generic Thank you card for her friend ‘Amanda’.

Use a with statement to generate this order. Have the with statement confirm the card is created by printing 'Card Generated!'.

6.
We want to verify whether or not the correct order was printed in the file. Use a with statement to open and read the file you just created in the last step.

Setting Up Personalized Greeting Cards
7.
Aisha’s Greetings also wants to print personalized cards! This means that customers can tell Aisha’s Greetings the words they want in their card and we can print them.

For personalized cards, let’s create a class-based context manager. First, create a class called personalized.

8.
Next, write a __init__ method that takes the sender’s and receiver’s names and saves them as attributes.

Add one more attribute that stores a newly opened (or created) file in write mode with the format < sender_name >_personalized.txt. This is the file we will be working on!

9.
Now, let’s set up what should happen when any new files are created and the context is started.

Make an __enter__ method that writes the receiver’s name to the opened file and returns that file. The format we write to the file should look like this: Dear < receiver>

10.
Lastly, let’s set up the final pieces of the customized card.

Create an __exit__ method that writes "Sincerely" followed by the sender’s name on the open file and then closes the file!

11.
Time to give our custom card generator a test run!

Aisha’s shop just got a customer 'John' who requested an order for a personalized card for his close friend 'Michael'.

John wants the body of the letter to say "I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always."

Use the context manager with a with statement to generate this order.

Aisha’s Greetings: Picking up speed!
12.
Aisha’s Greetings just got two orders from a customer named 'Josiah'.

He wants to get a generic birthday card for a colleague named 'Remy' and a personalized card for his sister 'Esther' that says:

"Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!“

Create a nested with statement that generates these orders in one call.

13.
Congrats! You were able to help Aisha’s Greetings create a system that generates cards quicker and smoother using the knowledge you gained about context managers!

Take some time to check out the great cards you created!
