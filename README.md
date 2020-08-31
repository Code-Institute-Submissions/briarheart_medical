# briarheart_medical
<<<<<<< HEAD
## Medication delivery database for Briarheart medial services  

The way I approached this project was “find a problem and solve it”.  I Accomplished this by noticing that to get though to my health centre to reorder prescriptions I need to call them several times as they are normally very busy, so I thought I could fix this by engineering a system to streamline the process. Instead of calling multiple times to get hold of a receptionist for them to take a note of my medications, my details and for what doctor, I built a system just for that. The Doctors are registered as they join the practice, patients register as they require the service. Patients then send a request to the doctors for medication who, then check to see if that is what they have received previously, if so, they can approve it. If not, they can decline it. The Patient gets an update in the form of a coloured notice on their profile home page where they can pay for the delivery charge for the medications to be sent to their home. Patients can view outstanding requests on their home page ie any they have made that haven’t been approved, approved and declined requests.

### UX

During the trial period we had a number of patients test the site these are their stories:


-	Samantha 
    - “ This app is amazing! I am a stay at home mum with 3 kids so trying to get to the phone is nightmare at times. I only find the time after the kids go to bed, but by that stage it was always too late, and the phone line shut. Now I can work with my children all day and re-order my medication at night so it can get delivered the day after, it has helped me so much. There have been periods in the past where I couldn’t get time to call and my medicine has runout. Now after just a few clicks that is a thing of the past”


- Derrick
    - “After an accident at work where some chemicals had damaged my voice I couldn’t speak for months, I was in terrible pain and was prescribed very strong pain killers. As this is a controlled substance, my wife couldn’t call up and reorder the prescription, I had to go down to the doctors and reorder it myself. Now I can just tap tap tap and they are on their way. This has helped me in so many ways. ”
 

All of the designs of my site can be view [here](…/wireframes/Wireframes.pdf)
 
I have tried as much as I could to stick to the wireframes, but during the creation process there had been some changes, namely the doctors index page no longer has its own statement. It shares the same as Patients.

## Features

This project has a lot of features that I am proud to point out

-	The traffic light system allows patients track individual requests ie green for approved like regular birth control pills, red for declined ie if a patient has been on pain medication too long and they need a check up to check if they have become addicted. And plain for pending to be seen by a medical professional. 
	

-	The doctors profile displays all the pending requests and is hidden after they have been actioned. It tells the doctor who is requesting the medication with how much. They can then approve or decline the request with 2 clicks, one to register choice and the next to confirm their choice. 
	

-	The login system is as simple as I could make it for the end users, I had previously considered a Patient log in and a Doctor log in. But That was simplified to a single log in page that filters content to different users needs. 
	

### Features Left to Implement

-	Directly link the medical database to users medical record and have it so that they can click and pay for ned meds, 
	

-	Set up a automatic reordering system, that will reorder medication and automatically charge the users card every time the medications are reordered. 


-	Have a second payment option, IE monthly prescription. For people who are on medication for the rest of their lives, ie diabetic patients on insulin. 


## Technolgies Used

For this project I have used the following technologies:


-	 [Javascript](https://www.javascript.com/)
        -	Javascript is used to give style and instruction to the payment button leading to stripe payment system
-	[Stripe](https://stripe.com/gb)
        -	Stripe is a payments processing infrastructure, It is used to take and handle card information safely and securely
-	[HTML]( https://html5.org/)
        -	Used to render elements of the website ie pictures or navigation links
-	[CSS]( https://www.w3.org/Style/CSS/Overview.en.html)
        -	Used to colour and set the elements apart from each other in the site

-	[Python]( https://www.python.org/)
        -	Used as the primary language to tell what buttons to do which functions, what each of those functions actually do and what is passed between mongo and my site

-	[Jinja]( https://jinja.palletsprojects.com/en/2.11.x/)
        -	Used this templating language in python which keeps the size of the overall site down and speeds up development overall

-	[Bootstrap]( https://getbootstrap.com/)
        -	Used their components as they are simple, easy to use and make the site look as beautiful as it can with as much functionality as I need.

-	[Django]( https://www.djangoproject.com/)
        -	This is the main technology used in my project. It is interwoven into all parts of it. It is  used to tell what information  be displayed on what pages. How movement between all pages is possible. 
   

## Testing

Samantha ordering meds:
1.	Click log on, enter incorrect passwords, waning message appears correctly
2.	Enter correct password, successfully directed to index page, success message with correct details appears, welcome statement and logo appears
3.	clicks on Add Medications, can not submit empty form, cannot leave out any fields, all are required correct message asking to Please fill in this field appears
4.	drop don only populates staff members – can no assign meds to other patients to verify
5.	redirected to index where correct information in success message appears ie Med_name dose and who for first and last name
6.	click profile, correct colour system for success, decline pending medicines appear.
7.	Purchase redirects to stripe payment correctly, error messages appear if no info or partial info appears – SUCCESS message appears after successful payment redirects to success page
8.	Click on back to profile button directs correctly takes back to profile, cancelled payment button takes to cancelled.html correctly back to profile works correctly
	

Derrick
1.	Click log on, enter incorrect passwords, waning message appears correctly
2.	Enter correct password, successfully directed to index page, success message with correct details appears, welcome statement and logo appears
3.	Traffic light system highlights what has been actioned correctly green for approved and red for declined. 
4.	Edit buttons autofill’s form correctly forms can be edited and saved repopulates with new info on profile page
5.	Delete verifies that the user wants to delete medicine, cancel takes back to index, delete button removes all together
	

Dr. Smith
1.	Log in form can not be left blank either entirely or partially – Password field replaces letters with stars correctly
2.	Username is case sensitive – gives incorrect log in waring if wrong case is entered
3.	 Accept button asks correctly if the doctor confirms that the doctor wants to do Accept request, decline also confirms correctly. Both cancel buttons on the confirmation page asks user back to their home page 


## Deployment



## Acknowledgements

- I recieved Inspiration from the project from my Mentor Rahul, he help me out tremedously with the log in issues i was having, as well as the Tutors at the code institute

- Strip payment had been a particular issue for me so I adapted a tutorial from "https://testdriven.io/blog/django-stripe-tutorial/" to suit my site. The Auther of the artical is Michael Herman

