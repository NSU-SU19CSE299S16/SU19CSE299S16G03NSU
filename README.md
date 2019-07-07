                                             
   ![NSU Logo](images/nsulogo.png)                                          
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                      
                                             
   ## Project Name: Populace
   ## Course Number: CSE 299
   ## Section:16
   ## Semester: Summer 2019
   ## Faculty Name: Shaikh Shawon Arefin Shimon
   ### Student Name: Sayeed Md. Shaiban
   ### Student ID: 1621193042
   ### Email: sayeed.shaiban@northsouth.edu
   ### Student Name: Monisha Saha
   ### Student ID: 1631667042
   ### Email: monisha.saha@northsouth.edu
   ### Date prepared: 11/06/2019
 -------------------------------------------------------------------------------

  
# Project Name: Populace
## Project Idea: 
> At present times we have various web based tools like google-classroom and piazza to manage resource with a large group of people. These are specially used by educational institutions (e.g. school, college, university) and other organization to communicate with a large number of people, to create workflow etc. But often using different sites simultaneously causes a lot of clutter and becomes cumbersome to keep track of. Hence we offer ‘Populace’ which is a web based application. The reason it stands out from the rest is because it will combine all this separate existing platform into one single platform. By signing in to ‘Populace’ users will be able to see posts made on the other existing web applications and also make their own query. It will therefore be a gathering place especially for students and for people who wants a one-stop solution to keep track of all the accounts in different web platform. Thus creating a better workflow. 
Primarily, the two platforms that we will include are ‘Google Classroom’ and ‘Piazza’. In the future we also plan to add other platforms similar to the above mentioned names.  

## Features:
>The main feature of ‘Populace’ is that users will be able to view different platforms on one window after logging in once. After that uses will be able to- 

   * Post:Users can post their questions, queries, problems which they wanted to post on specific platform from the site.
       Users will also be able to associate their subject/course to a specific platform.
   * They will also be able to see posts made on Google Classroom and piazza by others without changing the tab.
        
 ## Technology:
 >For UI design we decided to use Bootstrap. Bootstrap is a free and open-source CSS framework directed at responsive front-end web development. It contains CSS and JavaScript-based design templates for typography, forms, buttons, navigation and other interface components. Bootstrap will be used over the usual HTML and CSS.Due to npm api for piazza being old and unusable we have decided to switch our project from node.js to Django.For which our project specification has changed. Django is a high level python-based free and open-source web framework.Finally, for the database requirement we have opted to use a NoSQL database. And so we have decided to use MongoDB for the projects database requirement.  The reason for doing so is because we have only two entities:
        
   * USER: Will keep info about the users signing in the application
   * PLATFORM: The platform information for the signed in USER entity.
         
>To get the data from the other platforms we will be using the following APIs–

  * [Google Classroom Link](https://developers.google.com/classroom/)
  * [Piazza Link](https://www.npmjs.com/package/piazza-api) 
      
> Hence, our application technology stack stands as such –

## BussinessPlan/Monetization
>Google AdSense is the easiest way to monetize a website. It is designed for website developers to display photos, videos, texts on their website.  There are different types of ads available in Google AdSense. If our website is Google AdSense approved, Google will post ads on our website. Therefore, we can make money if someone clicks and views it. On the other hand, this can be used by universities, schools and colleges as a means for them to communicate with their students, so we can make these organizations use our website as their own personal site. It will help the students in their studies. Because they will find Google classroom and piazza in one platform. It will saves their time and keeps them organized. So we can also approach these educational institutions to adopt our site to their system.
         
         
         
         
        
        
