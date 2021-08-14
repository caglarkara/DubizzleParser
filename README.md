# DubizzleParser

Welcome to my tiny little helper project that I once implemented in frustration of catching the best bargain deails in used cars listed in the popular app Dubbizle in Dubai.

The problem with Dubizzle is being full of dealers that literally jump on any good bargain deal so as an end user your chances of catching a good car from a geniune seller is almost close to zero.
I personally noticed that every time I'm looking for a used car I was always late on calling the seller and this became my frustration. However till today (14/08/2021) Dubizzle still is your best chances to hunt and I need a solution!

Here comes it. I present you Dubizzle Parser (yes, a very lame name I agree, but kept calling it like this so I don't intent to change it now)


The system works in a very simple way.

This is a multi user platform.

Once the user enters Dubizzle web site, they are allowed to create their own query. In fact this feature of Dubizzle is quite nice with lots of option such as:
Price Range, Model Year Range, Seller Type, Body Type, etc. etc. etc.

So I thought replicating this is a stupid idea. 

Once you are done with your preferred filtering options, you come up with a list of cars that are available on the market. And the broswer search bar has all the filters that you have chosen. So in reality you can copy this url and paste it into another browser so you get your list of cars.

So now we know how to get our filters saved. By copying the search bar URL we'll keep them.

But even if we have the search url and the resulting page which is a ginourmous html page, so what?
Anyone who has dealt with coding a bit knows dealing with html is a very bad idea. First off, even if you use helper libraries, html comes with so many, so many tags, it is almost useless to do so.
So, I started examining the hmtl source code each time I submit my query. And the magic happened.

Right now, the search result html (for cars and classifieds only, not for real estate -14/08/2021) contains a Json formatted list that has everything we need! 
Thanks a million Dubizzle developers for designing it like this.

So now that we discovered that the result contains a Json formatted list; with the important bits like title, asking price, even the url to the ad itself! it is a matter of saving those results and sending the user a notification when we discovered a new car that fits into user's search criteria.

Of course, we don't want to spam the user with the same listings again and again, but handling this is piece of cake.


I decided to use a combination of Azure Logic Apps, Azure Tables and Azure Functions (python) in order to reach that goal. Because all these are very cool to use. Also dead cheap to use! 

I will try to explain the basic building blocks of the application here. 

The application consists of nnn Logic Apps:
1. dubizzleparser
    This logic app is the main part of the application. It will go through the queries table first. Then for each of the query it finds, it will call Dubizzle and parse the resulting html file. Since the result is dirty, it will first send it to the 
    function (TODO: Put the function name here) to remove everything and leave the Json alone.
    Then it will parse the results and check if it is an existing record in Listings table. If not, it inserts. 
2. notifsender: 
   This logic app is responsible to send the new entries to all the users. To avoid sending the same entities over and over again, the notification sender checks for the new found entities within the last 20 minutes. 

3.

One Function:
TODO: Place the function name here


3 Azure Tables:
1. Queries:
    This table is the main table that contains the queries created by the users.
    The fields are:
    "username",
    "queryName",
    "description",
    "dubizzleQuery"
    The usage of these fields are self explanatory.

2. Listings:
    This table holds the result of the query executions. The results are kept in this table forever (unless cleared from the table manually or by helper logic apps).
    The fields in this table are:
    "PartitionKey": This is the category (such as used cards, classfieds)
    "RowKey" : This is the title. Yes, we determine the record uniqueness by the title of the ad. Not the brightest idea I know.
    "Timestamp" : TODO: I don't know why this is here!
    "creationTS": The creation timestamp of the entry
    "price" : The listing price of the item
    "title" : Title again!
    "url" : The direct url to reach the listed item
    "userName" : The user to whom the result belongs.

3.  Users:
    This table keeps the user data.
    It has the following fields:
    "email": 
    "password": 
    "phone":
    "username": 

