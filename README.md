# Align Pilates

## About

Align Pilates is a Reformer Pilates Studio based in Limerick City. It is an e-commerce website created at a fundamental level to sell classes to the public, in B2C (business to consumer) business model. The webpage is created to allow users to see what classes are on offer in the studio, to book classes they would like to attend using Stripe Payments, regsiter for accounts, log into accounts if they are a user, have the option to ask questions about the studio and to read a little bit of what the studio is all about as well as a link to the studios Facebook page where users can choose to follow the studio there also. The core of the ethos of this studio is being open to everyone and anyone with an interest in taking part in Pilates, whether you are a beginner or a Pilates expert everyone is welcome in Align.

[Align Pilates live webpage can be accessed here](https://align-pilates-3ba4de4e758e.herokuapp.com/)

## Planning

### Why I Chose This Project
- I opted to create a Pilates booking website for my final project as I myself attend Pilates twice each week and it is something that I really love and am passionate about. I find the website and the app for my Pilates studio very impressive and provides a seamless user experience and I was hoping to create something similar for my own project. I created a mind map for myself of all of my ideas and features that could be potentially implemented to my project. I also created a short business model for Align Pilates at at planning stage so as to reinforce my project and to outline to trajectory I would like for the project to take.

![Mind Map](/media/mind-map-align-pilates.png)
![Business Model](/media/align-pilates-business-model.png)

### User Stories - Agile Methodology

- I was very conscoious at the start of this project that I did not want unneccessary features that did not add to the projects or that took up so much of my time that I feel it affected critical parts of my project. I knew the way I needed to plan and implememt this project was using an Agile Approach. With that in mind, I started at the smallest building block of Agile and I created my own table to illustrate user stories and to be able to track them as I progressed through the project to see that I was following in the correct direction for my project. I broke my User Stories up into three separate categories: Website Visitor, Site Owner and Studio Member.

    #### Website Vistor
    - From the aspect of a visitor to the webapge I wanted the website to be appealing to the eye, easy to navigate and open to users who would like to join to reach out and contact the studio also. 
    - I made the conscious decision of allow 'non members' to be able to book in for classes without having an account as for me in my day to day life I am often put off attending things when I have to fill out forms and provide a lot of personal information before I can attend something that I may only hvae the intention of attending just once.

    #### Site Owner
    - I did want the site owner/admin to be able to have enhanced functionality of being able to schedule classes, edit classes and delete classes as they so needed.
    - At a basic level I needed the site admin to be able to log in to the admin panel and have access to who has booked for each class.
    - I also wanted the site owner to be able to send emails to members and to potential new members who wish to join the studio.

    #### Studio Member
    - In keeping with my own studio I would like for members of the studio to be able to have enhanced functionality on the webpage. 
    - I wanted members to be able to view their booking history so they could see their class history.
    - I also wanted members to have a quick and easy transaction process so that they could easily book and attend classes, for that reason I allowed members to save and have the ability to update their personal details so there was minimal informaiton needed to make repeat bookings.

![Align Pilates User Stories](/media/align-pilates-user-stories.png)
![Align Pilates GitHub User Stories](/media/git-hub-user-stories.png)

### Site Goals
- Attractive to customer on initial opening of the webpage
- Easy to navigate throughout the website
- A fully functioning header with all working links to all pages throughout the webpage
- A straightforward and simple payment system for users to book classes and receive confirmation
- A selection of classes in a well laid out timetable that can easily be filtered and sorted through by users
- A contact form where users can include any questions and queries they may have
- Consistent use of styling and colours throughout the webiste
- A clear footer with a link to the studios Facebook page
- To allow users to register for an account easily if they wish to do so

## Features 
### Responsive Navbar
- The navbar I designed for Align Pilates is responsive to different screen sizes and different users who are using the webpage to allow for easiest navigation for website viewers as well as enhanced functionality for members and admin. 
- The site logo on the navbar is also a link that can be clicked on all pages to bring users back to the homepage.
- The navbar on larger screen sizes has multiple dropdown menu items to allow for users to filter class levels available, to either sign in or sign up if no one is signed into the webpage, for members to access their profile if they are signed in, for admin to access timetable management if they are signed in and for website visitors who are not members to choose if they would like to sign up or to contact the studio if they have any further questions. 
- The basket icons reflects to users if there is anything in their basket and the current total of their basket also.
- The mobile navbar displays for smaller screen sizes and displays as a compact menu item in the top left of smaller screens.
- When the mobile navbar is clicked the menu options are displayed to the user. This navbar is more concise than the main navbar so as to prevent the mobile navbar being too large or to require too much scrolling on smaller screens. There is no dropwdown on the mobile navbar other than the main one.

![Main Navbar](/media/main-navbar.png)
![Site Logo](/media/site-logo.png)
![Navbar Class List](/media/navbar-classes.png)
![Navbar Member View](/media/member-navbar-view.png)
![Navbar Admin View](/media/admin-navbar-view.png)
![Navbar Visitor View](/media/navbar-new-members.png)
![Navbar Basket](/media/navbar-basket.png)
![Mobile Navbar](/media/mobile-nav.png)
![Mobile Navbar Contents](/media/mobile-navbar-contents.png)

### Footer
- The footer remains consistent throughout all pages in the website. It is responsive for smaller and larger webpages. 
- The footer contains the site name as well as a link to the studio's webpage.

![Footer](/media/footer.png)

### Homepage
- The homepage is a landing page for all visitors to the Align Pilates website. The homepage consists of a large image of someone taking part in Reformer Pilates and a button to link users to the timetable for the studio.
- The homepage stays consistent with the styling of the webpage.

![Homepage](/media/homepage.png)

### About Page
- The about page provides a brief overview of the studio, its owners and it's ethos. There is a link in the "About Align Pilates" section for visitors to the site who would like to regsiter to become a member of the studio also.
- There is also a section of Kind Words from members of the studio in Bootstraps card layout giving their feedback and thoughts and feelings towards the studio. 
- At the end of the about page is an option for site visitors to sign up for the studios newsletter, this form was generated via MailChimp and is fully functional as tested.
- The about page is responsive for smaller and larger screens and maintains the styling from the homepage with regard to colour choices, fonts and keeping the same background images from the homepage.

![About Align Pilates](/media/about-align-pilates.png)
![Kind Words](/media/kind-words.png)
![Newsletter Subscription](/media/mail-chimp-newsletter.png)

### Classes Page
- The class page can be viewed by the users in an array of different formats based on sorting, filtering and search queries the user enters. From the homepage the user can choose to view all classses or to select their desired level of classes and view just those classes.
- On the classes page the classes are laid out in a card format displaying a snippet of information about each class including class name, teacher, rating, time, day, cost and a button to click on for users who wish to read more and book from there.
- Also on the class page is a search bar where users can enter a class name, teacher or day they would like to search for and results are displayed from there. 
- There is also a "Sort By" dropdown where users can choose to filter their class results by time, day of the week, teachers A-Z and ratings also. These filters can be applied in both filtering directions also to make it as easy as possible for users to find their desired class.
- There is also an option to "Arrange By" where users can opt to arrange the timetable by Class, Teacher, Time, Day or Rating.
- In order to make this page the most user friendly on smaller webpages I disabled the display of the search bar on smaller screens, however users could still filter classes from here.
- When the admin is signed in two extra options appear on each class card giving the admin the option to Edit or Delete any class in the timetable.
- The classses page is made responsive using Bootstrap column view to allow for less class cards on smaller screens and more on larger ones.
- There is also a 'Back to Top' button on the classes page to allow users to return to the top of the page whenever they need.

![Classes - Arrange By](/media/class-arrange-by.png)
![Classes - Search By](/media/class-search-results.png)
![Classes - Filter for Admins](/media/class-filter-admin.png)
![Classes - Filter for Visitors](/media/class-filter-visitor.png)
![Classes - Sort By](/media/class-sort-by.png)
![Classes Standard View](/media/class-standard-view.png)
![Classes Medium Screen View](/media/classes-medium-screen-view.png)
![Classes Mobile View](/media/classes-mobile-view.png)
![Back to Top Button](/media/back-to-top-button.png)

### Class Detail View
- Once the 'Book Now & More Info' button is clicked fomr the Classes Page users are brought to the Class Detail View.
- This is page created specifically for each different class available in the studio where it provides a more detailed description of each class to allow users to decide if a specific class is suitable for them and if they would like to attend. 
- This page also consists of other information about each class such as class level, teacher, cost, time, day and rating in a very clearly laid out and understandable format.
- This page also provides a message to people who are booking into classes in the studio alerting them to the fact that currently classes are only available to be booked on a weekly basis and that booking classes in advance of a week or longer is not currently possible in the studio. The note does advise users to complete the 'Contact Form' which is linked in the note, that if they would like to book further in advance and the studio would gladly oblige.
- The quantity is set here to 1 and this quantity cannot be increased or decreaesed by clicking the up or down button on the quantity arrows.
- At the end of the class detail view there is a three separate buttons, one to allow users to select to 'Continue Browsing' which brings users back to the class timetable view, a button to 'Book Now' which when clicked adds that specific class to the users basket and the last button 'Checkout' which allows users to go the the checkout and from there on to proceed to payment.
- When a user selects the 'Book Now' button a success toast message appears at the top right of the screen alerting users that the specific class they selected has been added to their basket.
- The user can select here to 'Go To Secure Checkout' from this toast message also.
- This page continues with the colour scheme and fonts used in all other pages on the website.
- This page is fully responsive and can be easily read and seen on smaller screen sizes as well as larger screens.

![Class Detail View](/media/class-detail-view.png)
![Class Detail Buttons](/media/class-detail-buttons.png)
![Clas Detail Link](/media/class-detail-link.png)
![Class Detail Mobile View](/media/class-detail-mobile.png)
![Class Detail Basket Toast](/media/class-detail-basket-toast.png)

### Basket
- The basket page can be accessed many ways in this webpage, as mentioned above it can be accessed via the toast message when users add something to their basket, view the class detail view and also via the navbar at the top right of the homescreen on larger screens and at the end of the dropdown on mobile screens.
- The basket provides users with a summary of what is in their basket and also presents users with the grand total for their order as well as an option to 'Remove' any items they may no longer require from their basket.
- If a users chooses to remove a specific class a custom toast message displays to highlight to users that that class has been removed.
- From here users can either choose to 'Continue Shopping' and return to the class timetable or to continue onto the 'Secure Checkout'.
- If users click to go to their bakset and it is empty a message displays to tell the user their basket is empty and provides a link for users to return to the timetable to look if they would like to book a class.
- For smaller screens the basket contents turned into a scrollable screen and a horizontal scrollbar can be seen at the end of the basket to allow users to view all the contents of their basket.

![Basket](/media/basket.png)
![Basket Item Removed Toast](/media/basket-remove-item.png)
![Empty Basket View](/media/empty-basket.png)
![Mobile View Basket](/media/mobile-view-basket.png)

### Checkout 
- Users are brought to this page once they have selected the 'Secure Checkout' button on either the basket page or when the basket icon is clicked in the navbar.
- Here users are brought to a checkout form where they have to enter the Name, Email Address, Phone Number, Card Number, Expiry Date, CVV2 and Post Code. 
- Also on this page a reservation summary is displayed to the user providing the details of the class name, time, day and cost as well as the total cost of the reservation.
- If a user is logged in on this page an option appears for users to save their information so it can be used again for their next booking. 
- If a user has not logged into their account there is a link for users to log in there and there is also a link for users who would like to create an account to do so here also.
- There is form validation on the checkout page displaying and error to users if incorrect card details are entered, an card expired is entered, if the email address is not entered in the correct format or if any fields are left blank. 
- Users also have the option here to 'Adjust Bag' where they can make any amendments needed to their orders they would like.
- Once the user has completed the form they select 'Complete Reservation' and users are brought to a loading page with a pale yellow colour and loading spinner so that the user knows their transaction is in progress.
- Users are then brought an order confirmation page including an order number and informing them that a confirmation email will be sent to their email address used shortly to confirm the booking. A toast success message also displays in the top right corner of the screen also indicating to the user that their reservation has been made as well as their order number and that a confirmation email will be sent to them soon.
- From here users can click on the link to navigate back to the timetable for the studio if they would like to continue browsing.
- All colours and fonts are maintained from the other pages on the webpage.

![Checkout](/media/checkout.png)
![Saved Info Checkout](/media/saved-info-checkout.png)
![Checkout Form Validation](/media/checkout-form-validation.png)
![Checkout Loading Spinner](/media/loading-spinner-checkout.png)
![Reservation Complete](/media/booking-complete.png)
![Reservation Toast Success Message](/media/toast-success-checkout.png)

### My Profile
- My Profile can be accessed by users from the Navbar when users are signed in by first clicking on 'My Account' and next selecting 'My Profile'.
- Here users can see a history of classes attended by members as well as users default saved information that can be updated by users at any point. 
- Users can select any previous reservation number and be taken to that previous booking and a toast message appears to highlight to users that this is a previous reservation and a confirmation email was sent at the time of booking.
- This page is fully responsive and switches from the user details and order history being laid out side by side to being stacked on top of one another on smaller screen sizes.

![Profile](/media/profile.png)
![Mobile Profile](/media/mobile-profile.png)
![Past Reservation Toast](/media/reservation-history-toast.png)

### Sign In
- Users can log into their account from a number of places within the website, they can access a 'Login' option by selecting 'My Account' on the navbar and clicking on 'Login' from here, they can choose to log in at the checkout page of the website and also there is a link for users to 'Log In' on the 'Sign Up' page if a user has mistakenly chose to create an account rather than signing into their account.
- Here users enter their username or email and password and can sign in from here.
- Users can check a checkbox if they would like their informaiton to be remembered for the next time they are signing in. 
- Once a user has signed in a toast message is displayed on the top right corner of the website to highlight to users that they are now signed in.
- Also on this page there is links for users who may have forgotten their password to reset it and another link for users who would like to access their homepage from here also.
- There is also a link here for users to 'Sign Up' if they need to sign up for an account rather than sign in. 

![Log In Page](/media/log-in.png)
![Log In Toast Message](/media/log-in-toast.png)

### Sign Out
- From the 'My Account' item on the navbar members can click here and select 'Sign Out' from the dropdown menu.
- From here users are brought to a screen to confirm the users intention to sign out as well as a link to return to the home page if this is not what the user wants.
- If the user clicks to 'Sign Out' a toast message is displayed in the top right corner of the screen display that the member has signed out.

![Sign Out Page](/media/sign-out.png)
![Logged Out Toast Message](/media/sign-out-confirmed.png)

### Join Now
- Users can choose to create an account with Align Pilates very easily from a number of different places in the website. They can access 'Join Now' from the navbar by selecting 'Want to Join?' and the choosing 'Join Now', also in the checkout users can select to 'Create an Account', from the 'Login' page there is a link to 'Sign Up' and also in the About page there is a link for users to 'Register'. 
- When any of these links are selected users are brought to the 'Sign Up' page where users only have to enter minial information to become a member, they need to enter and confirm their email, choose a username and enter and confirm their password also.
- Once users have complete this and passsed all required form validation the user is brought to a page informing them that they must confirm their email address by following a link that has been sent to their chosen email, a toast message appears in the top right hand corner indicating this also.
- Once this link is followed and users have confirmed their email this is reflected to the user and also appears in a toast message confirming so.
- Users are lastly brought to the 'Log In' page so the user can log in for the first time.

![Join Now](/media/sign-up.png)
![Verify Email](/media/verify-email.png)
![Confirm Email](/media/confirm-email.png)
![Email Confirmed](/media/email-confirmed.png)
![Redirect to Log In](/media/returned-to-login.png)


## Styling 
Overall, I am a big fan of less is more with styling so I tried to adopt and maintain that approach in the styling of this webpage.

### Colours
- As I had mentioned I am very much in awe of the Pilates Studio I attend I tried to choose colours similar to their webpage as well as colours that are present in the studio. I find these colours calming and very easy to read. I chose three colours at the start and used a mixture of those throughout the webpage. I used [Coloors](https://coolors.co/) to help me create my colour palette.

### Fonts 
- I used [Google Fonts](https://fonts.google.com/) to help me select a font for my webpage and also to be where I found my font of choice for the webpage. I selected Montserrat as the font for the webpage as I believe it to be elegant and very clearly read also.

### Media
- I opted with just the one background image for the entire webpage as I find now on a lot of webpages and in particular with respect to fitness and exercise pages a lot of them are jam packed with images of people illustrating how we should all want to look and the size we should be as well as what we should be doing. Pilates has a big focus on mindfulness amd it has taught me to appreciate me for who I am and to not compare myself to others. My joy in pilates comes from stretching my body and feeling strong within a movement and I couldn't find a more accurate picture than the one I had selected for my background image for the full website.
- I opted to change the opacity of this image on other pages on the website except the homepage as I wanted the content on the other pages to be the main focus for users whereas for the homepage I was happy for the background image to be the focus. 

![Header Image](/media/pilates-site-header.webp)

## Facebook Page
- I created a Facebook page as a source of marketing and advertising for Align Pilates using Facebook's "Pages" tab. In today's current climate social media seems to be the primary source of advertising for all businesses. It can be free and if businesses choose to pay for it it is still a relatively cheap method of advertising that can reach huge audiences.

![Facebook Page](/media/facebook-page-1.png)
![Facebook Page](/media/facebook-page-2.png)
![Facebook Page](/media/facebook-page-3.png)

## Technologies Used

- GitHub
- Django
- Python
- Stripe for secure payment processing
- Heroku for Deployment



## Future Features to Implement
- When time and skills allow I would like to change the option of booking pilates classes only on a weekly basis to a monthly basis on a calendar format if possible. I would like for users to be able to plan ahead and to be able to book ahead if needed.
- I would also consider putting blog posts on this webiste to enhance the community vibe of the studio and to really encourage maximum engagment from users and to increase the number of members in the studio also.
- I would also to to add enhanced form validation for the modificaiton of and adding classes to the studio timetable so that it is not possible for admins to book two classes at the same time. 