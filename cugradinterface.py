#!/usr/bin/python
# -*- coding: utf-8 -*-
# Database User Interface - Web version
#
# Note that these functions contain output
# such as print(), but do NOT contain any 
# actual database code. The database is handled by 
# a separate class.
#
# Also note that unlike the command-line version, you
# CANNOT USER input() because that waits for keyboard input.
# All input must come from CGI forms.
#

from cugraddb import CUgradDB

# Create a database object that will handle all the DB stuff.
dbobj = CUgradDB()

def listCourses():
    cur = dbobj.listCourses()
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""

    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    <table> 
    <tr><th>Course Name</th><th>Course Department</th><th>Course Level</th></th>
    """)

    for row in result:
        Name, Department, Level = row
        #print("%d %s" % (id, name))
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Name, Department, Level))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)  

def listMajors():
    cur = dbobj.listMajors()
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""

    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    <table> 
    <tr><th>Major Name</th><th>ID</th></th>
    """)

    for row in result:
        Name, Id = row
        #print("%d %s" % (id, name))
        print("<tr><td>%s</td><td>%s</td></tr>" % (Name, Id))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def listMinors():
    cur = dbobj.listMinors()
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""

    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    <table> 
    <tr><th>Minor Name</th><th>ID</th></th>
    """)

    for row in result:
        Name, Id = row
        #print("%d %s" % (id, name))
        print("<tr><td>%s</td><td>%s</td></tr>" % (Name, Id))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def listStudents():
    cur = dbobj.listStudents()
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""

    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    <table> 
    <tr><th>Last Name</th><th>First Name</th><th>Student ID</th><th>Username</th><th>Graduation Date</th></th>
    """)

    for row in result:
        Fname, Lname, Id, Username, GradSemester = row
        #print("%d %s" % (id, name))
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Fname, Lname, Id, Username, GradSemester))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)

def listPls():
    results = dbobj.listPls()
    
    print("<h1>PLS Requirements</h1><p>")
    
    print("""
    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    <table>
    <tr><th>Name</th><th>Id</th><th>
    """)
    for row in results:
        Id, Name = row       
        #print("%d %s" % (id, str(name)))
        print("<tr><td>%s</td><td>%s</td></tr>" % (Name, Id))
        print()
        
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 
        
def searchCourses(dept):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.searchCourses(dept)
    
    
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % dept)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...

        print("""
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        <table>
        <tr><th>Name</th><th>Department</th><th>Level</th></th>
        """)

        for row in result:
            Name, Department, Level = row       
            #print("%d %s" % (id, str(name)))
            print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Name, Department, Level))
            print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def insertCourse(Name, Department, Level):    
    dbobj.insertCourse(Name, Department, Level)   
    print("""

    <br>
    <a href="?">Return Home</a>
    
    """) 

def updatepls(name, plsid):    
    dbobj.updatepls(name, plsid)   
    print("""

    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def deleteStudent(sid):    
    dbobj.deleteStudent(sid)   
    print("""

    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def findMissingPls(Sid):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.findMissingPls(Sid)
    
    
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % Sid)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...

        print("""
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        <table>
        <tr><th>Missing PLS Requirements</th></th>
        """)

        for row in result:
            plsid = row       
            #print("%d %s" % (id, str(name)))
            print("<tr><td>%s</td></tr>" % (plsid))
            print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)

def findNewCourses(Sid):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.findNewCourses(Sid)
    
    
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % Sid)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...

        print("""
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        <table>
        <tr><th>Course Name</th><th>Department</th><th>Level</th></th>
        """)

        for row in result:
            Name, Department, Level = row       
            #print("%d %s" % (id, str(name)))
            print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Name, Department, Level))
            print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def deleteCourse(Department, Level):    
    dbobj.deleteCourse(Department, Level)   
    print("""

    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def insertStudent(Lname, Fname, Sid, Username, GradSemester):    
    dbobj.insertStudent(Lname, Fname, Sid, Username, GradSemester)   
    print("""

    <br>
    <a href="?">Return Home</a>
    
    """) 

def findIncompleteMajor(Sid):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.findIncompleteMajor(Sid)
    
    
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % Sid)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...

        print("""
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        <table>
        <tr><th>Department</th><th>Level</th></th>
        """)

        for row in result:
            Department, Level = row       
            #print("%d %s" % (id, str(name)))
            print("<tr><td>%s</td><td>%s</td></tr>" % (Department, Level))
            print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)

def insertMajor(Name, Mid):    
    dbobj.insertMajor(Name, Mid)   
    print("""

    <br>
    <a href="?">Return Home</a>
    
    """)

def insertMinor(Name, Mid):    
    dbobj.insertMinor(Name, Mid)   
    print("""

    <br>
    <a href="?">Return Home</a>
    
    """) 

def insertStudentMajor(Sid, Mid):    
    dbobj.insertStudentMajor(Sid, Mid)   
    print("""

    <br>
    <a href="?">Return Home</a>
    
    """) 

def searchStudentInfo(Sid):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.searchStudentInfo(Sid)
    
    
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % Sid)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...

        print("""
        <style>
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #dddddd;
        }
        </style>
        <table>
        <tr><th>First Name</th><th>Last Name</th><th>Student ID</th><th>Graduation Date</th><th>Major(s)</th><th>Minor(s)</th></th>
        """)

        for row in result:
            Fname, Lname, Id, GradSem, MajorId, MinorId = row       
            #print("%d %s" % (id, str(name)))
            print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Fname, Lname, Id, GradSem, MajorId, MinorId))
            print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)
        
def showDefaultPage(): 

    print("""

    <style>
    h1 {
        outline-style: solid;
    }

    div.a {
        outline-style: solid;
    }

    div.b {
        border: 1px solid red;
        outline-style: solid;
    }
    </style>
    <h1 align="center" style="color:rgb(255, 0,0);" >Welcome to C.U. Tracker</h1>

    <br>
    <font size="4"; color="black"><b>Explore your progress:</b></font>
    <br>
    <font size="2"; color="black"><b>Student Access</b></font><br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a style="text-decoration:none;rel="Click here" href="?listMajors=1"><font color="red">List all Majors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listMinors=1"><font color="red">List all Minors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listCourses=1"><font color="red">List all Courses</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?searchCourses=1"><font color="red">Search for Courses by Department</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?findNewCourses=1"><font color="red">Find Courses You Have Not Taken</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listPls=1"><font color="red">List all PLS Requirements</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?findMissingPls=1"><font color="red">Find Missing PLS Requirements</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?findIncompleteMajor=1"><font color="red">Find Missing Major Requirements</font></a>
    </ul>

    <br>
    <font size="4"; color="black"><b>Advisors Only:</b></font><br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a style="text-decoration:none;rel="Click here" href="?listStudents=1"><font color="red">List all Students</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listMajors=1"><font color="red">List all Majors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listMinors=1"><font color="red">List all Minors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listCourses=1"><font color="red">List all Courses</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?searchCourses=1"><font color="red">Search for Courses by Department</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listPls=1"><font color="red">List all PLS Requirements</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?findMissingPls=1"><font color="red">Find Missing PLS Requirements</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?findIncompleteMajor=1"><font color="red">Find Missing Major Requirements</font></a>
    </ul>

    <br>
    <font size="4"; color="black"><b>Registrar's Office Only:</b></font><br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <font size="3"; color="black"><b>Insert New Information</b></font><br>
    <li><a style="text-decoration:none;rel="Click here" href="?insertCourse=1"><font color="red">Insert a New Course</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?insertStudent=1"><font color="red">Insert New Student</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?insertMajor=1"><font color="red">Insert New Major</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?insertMinor=1"><font color="red">Insert New Minor</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?insertStudentMajor=1"><font color="red">Add Major for Student</font></a>
    
    <br><br><font size="3"; color="black"><b>Delete Existing Information</b></font><br>
    <li><a style="text-decoration:none;rel="Click here" href="?deleteCourse=1"><font color="red">Delete Course From Records</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?deleteStudent=1"><font color="red">Delete Student From Records</font></a>
    
    <br><br><font size="3"; color="black"><b>Update Existing Information</b></font><br>
    <li><a style="text-decoration:none;rel="Click here" href="?updatepls=1"><font color="red">Update PLS Name</font></a>

    <br><br><font size="3"; color="black"><b>Search Existing Information</b></font><br>
    <li><a style="text-decoration:none;rel="Click here" href="?listMajors=1"><font color="red">List all Majors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listMinors=1"><font color="red">List all Minors</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listCourses=1"><font color="red">List all Courses</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listStudents=1"><font color="red">List all Students</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?listPls=1"><font color="red">List all PLS Requirements</font></a>
    <li><a style="text-decoration:none;rel="Click here" href="?searchCourses=1"><font color="red">Search for Courses by Department</font></a>
    
    </ul>
    
    <p>    
    """)       
    
    
################################################################################
def showSearchCoursesForm():

    print("""
    <h2>Search for Courses</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="searchArtist" value="1">
    <table>
        <tr>
            <td>Course Department</td>
            <td><INPUT TYPE="TEXT" NAME="dept" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="Search Courses" value="Search!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showInsertCourseForm():

    print("""
    <h2>Insert Course</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertCourse" value="1">
    <table>
        <tr>
            <td>Course Name</td>
            <td><INPUT TYPE="TEXT" NAME="Name" VALUE=""></td>
        </tr>
        <tr>
            <td>Offering Department</td>
            <td><INPUT TYPE="TEXT" NAME="Department" VALUE=""></td>
        </tr>
        <tr>
            <td>Course Level</td>
            <td><INPUT TYPE="NUMBER" NAME="Level" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile2" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showUpdateplsForm():

    print("""
    <h2>Update PLS Name</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="updatepls" value="1">
    <table>
        <tr>
            <td>New PLS Name</td>
            <td><INPUT TYPE="TEXT" NAME="updatedName" VALUE=""></td>
        </tr>
        <tr>
            <td>PLS Id</td>
            <td><INPUT TYPE="TEXT" NAME="plsid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile3" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showdeleteStudentForm():

    print("""
    <h2>Delete Student From Records</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="deleteStudent" value="1">
    <table>
        <tr>
            <td>Enter Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="sid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile3" value="Delete!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showfindMissingPlsForm():

    print("""
    <h2>PLS Requirements Missing</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="searchArtist" value="1">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="Find Missing PLS Requirements" value="Track!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showfindNewCoursesForm():

    print("""
    <h2>Search for New Courses</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="searchArtist" value="1">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="Find Courses You Have Not Taken Yet" value="Find!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showdeleteCourseForm():

    print("""
    <h2>Delete Course From Records</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="deleteCourse" value="1">
    <table>
        <tr>
            <td>Enter Course Department and Level</td>
            <td><INPUT TYPE="TEXT" NAME="Department" VALUE=""></td>
            <td><INPUT TYPE="TEXT" NAME="Level" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile3" value="Delete!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showInsertStudentForm():

    print("""
    <h2>Insert Student</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertStudent" value="1">
    <table>
        <tr>
            <td>Student Last Name</td>
            <td><INPUT TYPE="TEXT" NAME="Lname" VALUE=""></td>
        </tr>
        <tr>
            <td>Student First Name</td>
            <td><INPUT TYPE="TEXT" NAME="Fname" VALUE=""></td>
        </tr>
        <tr>
            <td>Student ID Number</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr>
            <td>Student Username</td>
            <td><INPUT TYPE="TEXT" NAME="Username" VALUE=""></td>
        </tr>
        <tr>
            <td>Student Graduation Semester</td>
            <td><INPUT TYPE="TEXT" NAME="GradSemester" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile2" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showfindIncompleteMajorForm():

    print("""
    <h2>Major Requirements Missing</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="findIncompleteMajor" value="1">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="Find Missing Major Requirements" value="Track!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showInsertMajorForm():

    print("""
    <h2>Insert Major</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertMajor" value="1">
    <table>
        <tr>
            <td>Major Name</td>
            <td><INPUT TYPE="TEXT" NAME="Name" VALUE=""></td>
        </tr>
        <tr>
            <td>Major ID</td>
            <td><INPUT TYPE="TEXT" NAME="Mid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile2" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showInsertMinorForm():

    print("""
    <h2>Insert Minor</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertMinor" value="1">
    <table>
        <tr>
            <td>Major Name</td>
            <td><INPUT TYPE="TEXT" NAME="Name" VALUE=""></td>
        </tr>
        <tr>
            <td>Major ID</td>
            <td><INPUT TYPE="TEXT" NAME="Mid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile2" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showInsertStudentMajorForm():

    print("""
    <h2>Add Student Major</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertStudentMajor" value="1">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr>
            <td>Major ID</td>
            <td><INPUT TYPE="TEXT" NAME="Mid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile2" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

def showSearchStudentInfoForm():

    print("""
    <h2>Student Information</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="searchStudentInfo" value="1">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="Sid" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="Find Student Information" value="Find!">
            </td>
        </tr>
    </table>
    </FORM>

    <br>
    <a href="?">Return Home</a>
    """)

