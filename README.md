Air Route Finder (a model Application based on Travelling Salesperson Problem)
==============================================================================
The following application is a model application to demonstrate an alternate solution using Travelling Salesperson Problem.


How run the application
=======================
The following application requires Python , xlrd , xlwt , xlutils, sagemath installed in your system.

	1. Open up the terminal and your path to the repository /final_airroute
	2. Type in the terminal <pre>$ sh Air_Route.sh</pre>.
		The Script has following commands in it
		<pre> $ echo "Welcome to Air Route Finder Appication" </pre>
		<pre> $ echo "Please wait while Application is Loading" </pre>
		<pre> $ sage -ipython Air_Route_Finder.py </pre>
	3. Either Login to the Application or Sign up for the new account, (When Signed up the password will be received at your specified mail using smtp python module).
	4. Now at the Main Application select "File"-->"show City List" , this would open up libreoffice and would show an Adjacency matrix of all the cities distances to every other city (considering undirected complete graph).
	5. "File"-->"Open Previous Tour" will open up the image of the previous graph plotted.
	6. "File"-->"Find Tour" will find the tour travelling from the selected city , covering all the cities and coming back to the selected city.
	7. "Edit"-->"Update City List"-->"Add a City" will let you add the city , for better means open the city list at the side , Now the city that you will enter the City Name and its distances from all other cities present (seperated by comma) and hit Add City button this will add the city and its respective distances in the libreOffice Calc sheet.
	

Tech Stack
==========
	* Python Tkinter GUI, xlrd, xlwt, xlutils, sagemath
	* SQLite as DB

References
==========
	[1]  
	[2]
	[3]
