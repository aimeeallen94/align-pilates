# Align Pilates

![Am I Responsive Image](/media/am-i-responsive.png)

## About

Align Pilates is a Reformer Pilates Studio based in Limerick City. It is an e-commerce website created at a fundamental level to sell classes to the public, in B2C (business to consumer) business model. The webpage is created to allow users to see what classes are on offer in the studio, to book classes they would like to attend using Stripe Payments, register for accounts, log into accounts if they are a user, have the option to ask questions about the studio and to read a little bit of what the studio is all about as well as a link to the studios Facebook page where users can choose to follow the studio there also. At the moment the only marketing for this studio is solely from the Facebook page and via word of mouth from other clients of the studio. Further marketing strategies are to be implemented over time. The core of the ethos of this studio is being open to everyone and anyone with an interest in taking part in Pilates, whether you are a beginner or a Pilates expert everyone is welcome in Align.

** Please see below for note on Am I Responsive Mobile Image

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
    - I made the conscious decision of allow 'non members' to be able to book in for classes as well as being able to leave reviews without having an account as for me in my day to day life I am often put off attending things when I have to fill out forms and provide a lot of personal information before I can attend something that I may only have the intention of attending just once.

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

### Wireframes
- Using the collabrative design tool [Figma](https://www.figma.com) I created a number of wireframes for myself to create a vision of what I wanted the webpage to look like and how best to layout the various features within the webpage. 

## Homepage

![Homepage Wireframe](/media/homepage-wireframe.png)

## Mobile Homepage

![Mobile Homepage](/media/mobile-wireframe.png)

## About

![About Wireframe](/media/about-wireframe.png)

## Class View

![Class View Wireframe](/media/class-view-wireframe.png)

## Class Detail

![Class Detail Wireframe](/media/class-detail-wireframe.png)

## Basket

![Basket Wireframe](/media/basket-wireframe.png)

## Checkout

![Checkout Wireframe](/media/checkout-wireframe.png)

## Contact Us

![Contact Us Wireframe](/media/contact-us-wireframe.png)

## Features 
### Responsive Navbar
- The navbar I designed for Align Pilates is responsive to different screen sizes and different users who are using the webpage to allow for easiest navigation for website viewers as well as enhanced functionality for members and admin. 
- The site logo on the navbar is also a link that can be clicked on all pages to bring users back to the homepage.
- The navbar on larger screen sizes has multiple dropdown menu items to allow for users to filter class levels available, to either sign in or sign up if no one is signed into the webpage, for members to access their profile if they are signed in, for admin to access 'Add Class' if they are signed in and for website visitors who are not members to choose if they would like to sign up or to contact the studio if they have any further questions. 
- The basket icons reflects to users if there is anything in their basket and the current total of their basket also.
- The mobile navbar displays for smaller screen sizes and displays as a compact menu item in the top left of smaller screens.
- When the mobile navbar is clicked the menu options are displayed to the user. This navbar is more concise than the main navbar so as to prevent the mobile navbar being too large or to require too much scrolling on smaller screens. There is no dropwdown on the mobile navbar other than the main one.

![Main Navbar](/media/main-navbar.png)
![Site Logo](/media/site-logo.png)
![Navbar Class List](/media/navbar-classes.png)
![Navbar Member View](/media/member-navbar-view.png)
![Navbar Admin View](/media/admin-my-account-dropdown.png)
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
- On the classes page the classes are laid out in a card format displaying a snippet of information about each class including class name, teacher, time, day, cost and a button to click on for users who wish to read more and book from there.
- Also on the class page is a search bar where users can enter a class name, teacher or day they would like to search for and results are displayed from there. 
- There is also a "Sort By" dropdown where users can choose to filter their class results by time, day of the week and teachers A-Z also. These filters can be applied in both filtering directions also to make it as easy as possible for users to find their desired class.
- There is also an option to "Arrange By" where users can opt to arrange the timetable by Class, Teacher, Time or Day.
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
- Once the 'Book Now & More Info' button is clicked from the Classes Page users are brought to the Class Detail View.
- This is page created specifically for each different class available in the studio where it provides a more detailed description of each class to allow users to decide if a specific class is suitable for them and if they would like to attend. 
- Also available on this page is the option for users to leave a review for a specific class as well as the option to read any reviews that have been left for this class also.
- The ratings and review form consists of the following fields: class name, star rating, review and author.
- This form consists of validation that only allows users to submit a review with a star rating of 0 to 5. It also consists of validation that the form cannot be submitted unless all fields have been completed.
- The reviews are displayed in a card format and have the information clearly displayed consisting of class name, review, star rating, author and date. 
- This page also consists of other information about each class such as class level, teacher, cost, time, day and an average overall rating (calculated as an average figure form users ratings or displaying 'No Rating' if no ratings have been left) in a very clearly laid out and understandable format.
- This page also provides a message to people who are booking into classes in the studio alerting them to the fact that currently classes are only available to be booked on a weekly basis and that booking classes in advance of a week or longer is not currently possible in the studio. The note does advise users to complete the 'Contact Form' which is linked in the note, that if they would like to book further in advance and the studio would gladly oblige.
- The quantity is set here to 1 and this quantity cannot be increased or decreaesed by clicking the up or down button on the quantity arrows.
- At the end of the class detail view there is a three separate buttons, one to allow users to select to 'Continue Browsing' which brings users back to the class timetable view, a button to 'Book Now' which when clicked adds that specific class to the users basket and the last button 'Checkout' which allows users to go the the checkout and from there on to proceed to payment.
- When a user selects the 'Book Now' button a success toast message appears at the top right of the screen alerting users that the specific class they selected has been added to their basket.
- The user can select here to 'Go To Secure Checkout' from this toast message also.
- This page continues with the colour scheme and fonts used in all other pages on the website.
- This page is fully responsive and can be easily read and seen on smaller screen sizes as well as larger screens.

![Class Detail View](/media/class-detail-view.png)
![Class Detail Buttons](/media/class-detail-buttons.png)
![Class Detail Link](/media/class-detail-link.png)
![Class Detail Mobile View](/media/class-detail-mobile.png)
![Class Detail Basket Toast](/media/class-detail-basket-toast.png)
![Rating Form](/media/rating-form.png)
![Rating Cards](/media/rating-cards.png)
![Rating Form Validation Blank Field](/media/rating-form-validation.png)
![Rating Form Validation - Success Toast](/media/rating-form-success-toast.png)
![Rating Form - Error Message](/media/rating-form-error-message.png)

### Admin Functionality - Class Amendment, Deletion and Addition - Full CRUD Functionality
- When the admin is signed into the studio as mentioned above in the class view and class detail and navbar different options appear for admin users. These are the ability to modify the timetable. Admins have the option to add, edit and delete classses. 
- Admins can edit and delete classes directly from the class timetable view when they select the edit or delete option.
- It is reflected to the admin in the form of a toast message to highlight to admins they are are editing a specific class.
- The admin is displayed a form of all the class informaiton in fields and can edit each one as they choose.
- Once they are happy with all fields they have amended and select to 'Update Class' a toast message appears to alert the admin that the class was edited and the admin is returned to the Class Detail view of that specific class.
- If an admin wishes to delete a class they can do so by selecting the delete button on the timetable view of a specific class or on the class detail view of a class.
- Admins are they displayed a toast message confirming the class was deleted in the form of a toast message.
- If the admin wishes to add a class and does so view the navbar they are once again displayed a form with fields to complete similar to the edit form but all fields are blank here.
- For the class day number on both the edit and add class forms there is a note to highlight to admins to assign the day number accordingly to allow for accurate sorting of classes by day for studio clients.
- Once the admin has completed all fields and selected to add class a toast message once again is displayed to highlight to the admin that the class has been added and they are returned to the class detail of that class.

![Edit Form - 1](/media/edit-class-form.png)
![Edit Form - 2](/media/edit-class-form-2.png)
![Editing Toast](/media/edit-toast-message.png)
![Class Updated Toast](/media/update-class-toast.png)
![Return to Class Detail](/media/class-detail-return.png)
![Delete Toast](/media/delete-toast-message.png)
![Add Class Form - 1](/media/add-class-form.png)
![Add Class Form - 2](/media/add-class-form-2.png)
![Add Class Toast](/media/add-class-toast.png)

### Admin Panel
- The admin panel can be accessed only by admins and this can be used to edit, add and delete classes also.
- The admin can also see the details of the Contact Us Form which is available to be completed by any visitor of the website. 
- Also in the admin panel site owners can modify and delete any ratings as needed.
- The admin panel has the extra functionality of being able to add more class levels which cannot be done directly from the webiste.
- In the admin panel admins can also see all users who have accounts with Align Pilates and can also verify email addresses directly from here if required.
- From the admin panel admins can also view all reservations made in the studio and the details of the reservation also.
- From here admins can modify and delete and reservations as needed.

![Admin Panel](/media/admin-panel-home.png)
![Admin Panel - Level List](/media/admin-panel-levels-list.png)
![Admin Panel - Class List](/media/admin-panel-class-view.png)
![Admin Panel - Reservaiton List](/media/admin-panel-reservation-list.png)
![Admin Panel - Reservation View](/media/admin-panel-reservation.png)
![Admin Panel - Reservation View - 2](/media/admin-panel-reservation-2.png)
![Admin Panel - Ratings List](/media/admin-panel-ratings-list.png)
![Admin Panel - Ratings Detils](/media/admin-panel-ratings-details.png)
![Admin Panel - Contact Us Details](/media/contact-us-details-admin-panel.png)


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

### Contact Us
- On the navbar there is an option for visitors to the website to fill out a 'Contact Us' form. This form allows site asks users to fill in their name, email address, contact number and a brief message where users can ask any questions or queries they may have before joining the studio.
- The link to this contact us form is also found in the class detail view for anyone who would like to book for multiple classes in the studio.
- This form has form validation in it and will ask prompt users to fill in any blank fields or incorrectly filled once such as the email address not filled in in an email format.
- Users will be returned with a toast message in the top right corner of the screen once they fill out the form informing them that their message has been sent and the studio will reply to them shortly. 
- Users are returned to the studios homepage once the form is submitted.
- Users completed forms are saved to the admin panel as 'Contact Details' for the site owner to be able to view and take action upon these queries from here. 

![Contact Us Form](/media/contact-us-form.png)
![Contact Us Form Toast Message](/media/contact-form-submitted.png)
![Contact Us Details Admin Panel](/media/contact-us-details-admin-panel.png)

### Custom 404 Page
- If a user selects a page that is no longer there, a page that is 'broken' or enter an address at the end of the site url that doesn't exist a custom 404 page displays to the user to inform them that the page they are looking for doesn't exist and a link is provided to return to the homepage from here.
- This custom 404 page is display when a 404 error is returned by the server instead of the standard 404 error page.

![Custom 404 Page](/media/custom-404.png)

## Am I Responsive Mobile Image
- I noted when I made my Am I Responsive Image that my mobile view header of my homepage was slightly blocked by my navbar, however it wasn't when I was looking at it locally or in production. 
- I have inserted a screenshot below of how it appears in Chrome DevTools on smaller screens which looks perfect and the header it not being blocked by anything in this.

![Mobile View Homepage](/media/mobile-view-home-page.png)

## Styling 
- Overall, I am a big fan of less is more with styling so I tried to adopt and maintain that approach in the styling of this webpage. 
- As mentioned above in my spare time I attend a local Pilates studio twice a week which I absolutely adore so I did take a lot of my inspiriation from the studio I go to both from their studio and website. Their studio and webpage are both very simply designed and maintain consistent styling throughout so I tried to echo that in my design of this website.
- I am also just finishing renovating a house and for this project I took a very deep dive into deisgn and style ideas for a home and the more I looked the more I was convinced that I am a fan of less is more and to also maintain more traditional styling so that what I create will definitely stand the test of time and not look old and dated in a matter of months.

### Colours
- As I had mentioned I am very much in awe of the Pilates Studio I attend I tried to choose colours similar to their webpage as well as colours that are present in the studio. I find these colours calming and very easy to read. I chose three colours at the start and used a mixture of those throughout the webpage. I used [Coloors](https://coolors.co/) to help me create my colour palette.
- I wanted all of the colours to clearly contrast against one another but was not happy to use a standard black and white to contrast against the teal colour I chose so I took my time to select an off white and a dark grey to provide an appropriate contrast.

### Fonts 
- I used [Google Fonts](https://fonts.google.com/) to help me select a font for my webpage and also to be where I found my font of choice for the webpage. I selected Montserrat as the font for the webpage as I believe it to be elegant and very clearly read also. I wanted users to be able to easily read all content on the webpage so I am very happy with the font I selected. I wanted it to be a timeless font so avoiding using something that appeared to be a current trend at the time when this website was created.

### Media
- I opted with just the one background image for the entire webpage as I find now on a lot of webpages and in particular with respect to fitness and exercise pages a lot of them are jam packed with images of people illustrating how we should all want to look and the size we should be as well as what we should be doing. Pilates has a big focus on mindfulness amd it has taught me to appreciate me for who I am and to not compare myself to others. My joy in pilates comes from stretching my body and feeling strong within a movement and I couldn't find a more accurate picture than the one I had selected for my background image for the full website.
- I opted to change the opacity of this image on other pages on the website except the homepage as I wanted the content on the other pages to be the main focus for users whereas for the homepage I was happy for the background image to be the focus. 

![Header Image](/media/pilates-site-header.webp)

## Facebook Page
- I created a Facebook page as a source of marketing and advertising for Align Pilates using Facebook's "Pages" tab. In today's current climate social media seems to be the primary source of advertising for all businesses. It can be free and if businesses choose to pay for it it is still a relatively cheap method of advertising that can reach huge audiences.

![Facebook Page](/media/facebook-page-1.png)
![Facebook Page](/media/facebook-page-2.png)
![Facebook Page](/media/facebook-page-3.png)

## Testing

### HTML Testing
- When testing the deployed website link through the [W3 HTML Validator](https://validator.w3.org/) it all passed and no errors or warnings were displayed.

![HTML Testing](/media/html-testing.png)

### CSS Testing
- Similarly, when the CSS files where ran through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) all files passed through and no errors or warnings displayed.

![CSS Testing](/media/css-testing.png)

### Python Testing
- I used Flake8 which was already installed in my workspace to test all of my python files in my project directly from the terminal.

### Lighthouse Testing
- When the website was tested on Chrome DevTools Lighthouse testing I am pleased to say it performed well across all categories.

![Lighthouse Testing](/media/lighthouse-testing.png)

### Manual Testing
- I completed manual testing by going through each page on the website, clicking all links, completing all forms, adding to baskets, completing all admin functionality and overall working from start to finish on the webiste ensuring all features were working. 

![Manual Testing](/media/manual-testing-1.png)
![Manual Testing](/media/manual-testing-2.png)

## Deployment 
- I completed the deployment of my project using the Code Institute's Deployment steps in the Boutique Ado project

### Elephant SQL as Database
- As I have an account with Elephant SQL I signed into my account and opened my dashboard. 
- From here I seleceted to 'Create New Instance'. I followed the steps here to create my instance giving it a name, a region, a tier and reviews the details provided. When happy with these I selected to Create Instance. 
- I could now access this instance from my dashboard. I clicked on the instance I had just created and from here I copied the database URL.

### Heroku 
- As I also have an account with Heroku I logged into my Heroku account and once again navigated to my dashboard.
- In my dashboard I selected 'New' and then chose to 'Create a new app'. I gave my app a name and selected it's region. I then clicked to 'Create App'.
- I navigated back to my dashboard again and selected my new app I had created. I selected the Settings tab here and scrolled down to 'Reveal Config Vars'. Here I added in my DATABASE_URL in the KEY field and added my database url I had earlier copied from my Elephant SQL and pasted it in here.
- In the deploy tab I enabled automatic deploys so that a new app would be created each time I pushed to GitHub. I had to connect to my own GitHub for this and selected the repository I wanted to use for this.
- I generated a secret key and added it to the config vars.

### Gitpod
- Back in my terminal I installed dj_database_url==0.5.0 and psycopg2 so I could connect to my external database.
- I used the command 'pip freeze > requirements.txt' to add these requirements to my requirements.txt file.
- I also added import os and import dj_database_url to my settings.py file.
- I created an if else statement in my settings.py file to connect to my external database when run in Heroku and to connect to my local one when run in Gitpod.
- I showed and made my migrations from these changes.
- In the terminal I created a new superuser for my external database.
- In the terminal I installed gunicorn to act as my webserver and added this to my requirements.txt file also.
- I created a Procfile and added the following code to it 'web: gunicorn align_pilates.wsgi:application'.
- I logged into heroku via my terminal and temporarily disabled collectstatic.
- I added the hostname of my heroku app and 'localhost' to my ALLOWED_HOSTS in my settings.py file.
- I pushed these changes to GitHub and from my terminal I deployed to Heroku using 'git push heroku main'.
- I changed my secret key in settings.py so that my secret key would be gotten from the environment.

### AWS Amazon Web Services
- I created an account with AWS and filled in all necessary forms. Once I logged in I navigated to the AWS Management Console and seacrhed for S3 and opened it.
- In S3 I selected to 'Create Bucket' named it after my Heroku app, selected my region, set object ownership to ACLs enabled and Bucket Owner Preferred and unchecked the 'Block All Public Access' box and next selected to 'Create Bucket'.
- In the bucket I just created I selected it and clicked on its properties tab and activated the bucket for static website hosting and entered in some default values for the index and error documents and saved them. 
- I next navigated to the permissions tab and I pasted in the follows CORS Configuration 
"[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]"
- In the Bucket Policy Tab I selected Policy Generator. Here I selected the policy type to be 'S3 Bucket Policy', entered * for principals to allow all principals and selected the action to be GetObject. I copied the ARN from the Bucket Policy tab and pasted it in for the ARN value. I selected to 'Add Statement' and next 'Generate Policy'. I copied the policy genertated and pasted it into the Bucket Policy and added a /* to the end of the resource key to allow access to all resources in the bucket. I saved this.
- In the Access Control List, I selected to edit and enabled list for Everyone, accepting the warning also.
- Back in the AWS Management Console I searched for IAM and selected it. In the dropdown at the side I selected User Groups and created a group.
- Here I next created a polciy by selected Policy > Create Policy. Here I selected Actions > Import Policy and searched for s3 and selected the AmazonS3FullAccess policy. From here I returned to copy my ARN from s3. I pasted this into the AmazonS3FullAccess policy into the resources, once on its own and the second time followed by /*. I then selected 'Review Policy', gave it a name and description and then selected to 'Create Policy'.
- Once that policy has been created I am returned to the main policy page, from here I navigate back to the User Groups page so that I can attach the policy I just created to my group. I select my group, select 'Attach Policy', search for the policy I just created, select it and select 'Attach Policy'.
- Once that is done I select users from the menu at the side to create a user. I select 'Add User' and name it ending in staticfiles-user and give the user programmatic access and I add that user to my group and create user.
- To get the CSV file to download I select users, click on the user I just created and selected the 'Security Credentials' tab and scrolled down to Access Keys and selected to create access key and I selected 'Application Running Outside AWS'. I selected the create the access key and clicked to download csv when ready.

### GitPod
- Back in my GitPod terminal I installed boto and django-storages and freezed these into my requirements.txt file.
- In my settings.py file I added storages to my installed apps.
- Also in my settings file I added an if statement for django to use AWS S3 buckets for storages only when connected to Heroku. I added my aws bucket name in settings.py also.
- To let django know that in production we want it to use s3 to store static files we start by creating a file called custom_storages.py in the root directory of my project. Here I imported settings from django.conf and S3BotoStorage from storages.backends.s3boto3. I created a custom class here for static and media storage.
- In my settings.py file I wrote the code to show where we want out static and media files stored as defined in our custom_storages we just created.
- Here I also override the urls for static and media files so that it was clear they were both to be stored in S3 in production.

### Heroku 
- Back in Heroku I returned to my app, accessed setting and reveal config vars and added my AWS access key and secret key here. I also added USE_AWS and set it it to true here.
- In heroku I added my stripe public key, secret key and webhook secret signing key to allow for stripe to be successfully used when in production also.

- I pushed my code to github and as a result of automatic deploys a new app was deployed in Heroku also.

### AWS
- As a result of my changes to GitPod static files are now being stored in AWS buckets and a static folder has been created in the bucket as a result.
- I next created a media folder here. I uploaded my header site image to here and granted public read access to them and uploaded them.

- I deployed my project to Heroku once more, tested payments, webhooks, static and media files and all were now working successfully!

## Technologies Used

- GitHub for version control
- GitPod
- Django for web framework
- Stripe for secure payment processing
- Heroku for Deployment
- Google/Chrome Developer Tools
- Lucidchart
- Apple Numbers for Spreadsheet/Table creation
- AWS
- Figma for Wireframes

## Django Packages Used

- Gunicorn
- Allauth
- Crispy Forms
- DJ-database-url
- Oauth
- Boto-3
- Django Storages

## Languages Use 

- Python
- HTML
- CSS 
- Javascript

## Problems I encountered 
- Throughout the creation of this website I thouroughly enjoyed myself but equally I found it an extremely humbling experience.
- I encountered numerous stumbling blocks and problems throughout this project.
- One in particular I feel like I learned a lot from was when it came to creating my custom 404 page, I created the page fine, set up my views and urls without issue however I could not get a 404 error message to display on my webite. The only error message that would display was a 500 error which was indicating that I had an internal server error which I did not know I had!
- Thankfully due to Chrome DevTools I could see that it was pointing to a favicon error.
- I realised that I needed to create an icon to display on the browser tab of my website. I maange to do this and implement it so my site now has a lovely icon image and I got rid of the internal server error and I could get a 404 error to display so I could render my custom 404 page!
- I also encountered an issue on the admin panel that when users made a booking on the admin panel two reservations were displaying, only one of these had a stripe PID, only one email was sent to users to confirm the booking and only one stripe payment was processed. I delved into this issue and found after many hours of troubleshooting that I had had a typo in a variable name.

## Future Features to Implement
- When time and skills allow I would like to change the option of booking pilates classes only on a weekly basis to a monthly basis on a calendar format if possible. I would like for users to be able to plan ahead and to be able to book ahead if needed.
- I would also consider putting blog posts on this webiste to enhance the community vibe of the studio and to really encourage maximum engagment from users and to increase the number of members in the studio also.
- I would also to to add enhanced form validation for the modificaiton of and adding classes to the studio timetable so that it is not possible for admins to book two classes at the same time. 

## Credits 
- This site was insipred by Code Institures Boutique Ado project with my own twists added to it. 
- This site was also heavily inspired by the Pilates Studio I attend in my personal life [Glow Pilates](https://glowpilates.ie/)
- The site header image was taken from a [Vogue Artcile](https://www.vogue.com/article/reformer-pilates-guide) about pilates.
- Colours for the website were selected from [Coloors](https://coolors.co/).
- The font Montserrat was taken from [Google Fonts](https://fonts.google.com/).

## Thank you
- A special thanks to my mentor Luke Buchanan for his help throughout this project and course. 
- A big thank you to Tutor Support in Code Institute for all of their help within any problems I ran into throughout this project.
- A thank you to Student Care who were so approachable with any issues I had throughout the course and very reassuring and understanding with any problems I encountered.
- Thank you to Amy my cohort facilitator for her kindness and encouragement thorought my PP5. 
- Thank you to the ETB and Code Institute for providing this course and really allowing me to believe in myself and my abilities to write code and really really enjoy doing it.