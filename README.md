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
- The navbar on larger screen sizes has multiple dropdown menu items to allow for users to filter classes available, to either sign in or sign up if no one is signed into the webpage, for members to access their profile if they are signed in, for admin to access timetable management if they are signed in and for website visitors who are not members to choose if they would like to sign up or to contact the studio if they have any further questions. 
- The basket icons reflects to users if there is anything in their basket and the current total of their basket also.
- The mobile navbar displays for smaller screen sizes and displays as a compact menu item in the top left of smaller screens.
- When the mobile navbar is clicked the menu options are displayed to the user. This navbar is more concise than the main navbar so as to prevent the mobile navbar being too large or to require too much scrolling on smaller screens. There is no dropwdown on the mobile navbar other than the main one.

![Main Navbar](/media/main-navbar.png)
![Site Logo](/media/site-logo.png)
![Navbar Class List](/media/navbar-classes.png)
![Navbar Member View](/media/member-navbar-view.png)



## Styling 
Overall, I am a big fan of less is more with styling so I tried to adopt and maintain that approach in the styling of this webpage.

### Colours
- As I had mentioned I am very much in awe of the Pilates Studio I attend I tried to choose colours similar to their webpage as well as colours that are present in the studio. I find these colours calming and very easy to read. I chose three colours at the start and used a mixture of those throughout the webpage. I used [Coloors](https://coolors.co/) to help me create my colour palette.

### Fonts 
- I used [Google Fonts](https://fonts.google.com/) to help me select a font for my webpage and also to be where I found my font of choice for the webpage. I selected Montserrat as the font for the webpage as I believe it to be elegant and very clearly read also.

### Media
- I opted with just the one background image for the entire webpage as I find now on a lot of webpages and in particular with respect to fitness and exercise pages a lot of them are jam packed with images of people illustrating how we should all want to look and the size we should be as well as what we should be doing. Pilates has a big focus on mindfulness amd it has taught me to appreciate me for who I am and to not compare myself to others. My joy in pilates comes from stretching my body and feeling strong within a movement and I couldn't find a more accurate picture than the one I had selected for my background image for the full website.

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