#!/usr/bin/python
# -*- coding: utf-8 -*-
# "she-bang" line is a directive to the web server: where to find python
#
# filename: ctunes.py
# cTunes = Clark Tunes = mini iTunes?

import time
import cgi
import cgitb; cgitb.enable()
import cugradinterface

################################################################################
def doHTMLHead():

    print("""
    <html>
    <head>
    <style>
body  {
    background-image: url("bggg.jpg");
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position:center;
}
</style>
    <title>CU Tracker</title>
    </head>
    </body>
    """)


################################################################################
def doHTMLTail():

    print("""
    <p>
    <hr>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime())


################################################################################
if __name__ == "__main__":

    print("Content-Type: text/html; charset=utf-8")
    print("Cache-Control: no-cache, must-revalidate") # HTTP/1.1 
    print("Expires: Sat, 26 Jul 1997 05:00:00 GMT") # Date in the past 
    print()

    form = cgi.FieldStorage()
    
    doHTMLHead()

    #print("<br><br>")
    #print("Debugging mode with 'print form':<br>")
    #print(form)
    #print("<br><br>")

   
    if "listCourses" in form:       
        cugradinterface.listCourses()

    elif "listMajors" in form:
        cugradinterface.listMajors()

    elif "listMinors" in form:
        cugradinterface.listMinors()

    elif "listStudents" in form:
        cugradinterface.listStudents()

    elif "listPls" in form:
        cugradinterface.listPls()      
        
    # search for a name, and we have the name
    elif "searchCourses" in form and "dept" in form:
        dept = form["dept"].value 
        cugradinterface.searchCourses(dept)
       
    # search for a name, and we DO NOT have the name
    elif "searchCourses" in form:
        cugradinterface.showSearchCoursesForm()

    elif "insertCourse" in form and "Name" in form  and "Department" in form and "Level" in form:
        Name = form["Name"].value
        Department = form["Department"].value
        Level = form["Level"].value
        cugradinterface.insertCourse(Name, Department, Level)

    elif "insertCourse" in form:
        cugradinterface.showInsertCourseForm()

    elif "updatepls" in form and "updatedName" in form  and "plsid" in form:
        updatedName = form["updatedName"].value
        plsid = form["plsid"].value
        cugradinterface.updatepls(updatedName, plsid)

    elif "updatepls" in form:
        cugradinterface.showUpdateplsForm()

    elif "deleteStudent" in form and "sid" in form:
        sid = form["sid"].value
        cugradinterface.deleteStudent(sid)

    elif "deleteStudent" in form:
        cugradinterface.showdeleteStudentForm()

    elif "findMissingPls" in form and "Sid" in form:
        Sid = form["Sid"].value 
        cugradinterface.findMissingPls(Sid)

    # search for a name, and we DO NOT have the name
    elif "findMissingPls" in form:
        cugradinterface.showfindMissingPlsForm()

    elif "findNewCourses" in form and "Sid" in form:
        Sid = form["Sid"].value 
        cugradinterface.findNewCourses(Sid)

    # search for a name, and we DO NOT have the name
    elif "findNewCourses" in form:
        cugradinterface.showfindNewCoursesForm()

    elif "deleteCourse" in form and "Department" in form and "Level" in form:
        Department = form["Department"].value
        Level = form["Level"].value
        cugradinterface.deleteCourse(Department, Level)

    elif "deleteCourse" in form:
        cugradinterface.showdeleteCourseForm()

    elif "insertStudent" in form and "Lname" in form  and "Fname" in form and "Sid" in form and "Username" in form and "GradSemester" in form:
        Lname = form["Lname"].value
        Fname = form["Fname"].value
        Sid = form["Sid"].value
        Username = form["Username"].value
        GradSemester = form["GradSemester"].value
        cugradinterface.insertStudent(Lname, Fname, Sid, Username, GradSemester)

    elif "insertStudent" in form:
        cugradinterface.showInsertStudentForm()

    elif "findIncompleteMajor" in form and "Sid" in form:
        Sid = form["Sid"].value 
        cugradinterface.findIncompleteMajor(Sid)

    # search for a name, and we DO NOT have the name
    elif "findIncompleteMajor" in form:
        cugradinterface.showfindIncompleteMajorForm()

    elif "insertMajor" in form and "Name" in form  and "Mid" in form:
        Name = form["Name"].value
        Mid = form["Mid"].value
        cugradinterface.insertMajor(Name,Mid)

    elif "insertMajor" in form:
        cugradinterface.showInsertMajorForm()

    elif "insertMinor" in form and "Name" in form  and "Mid" in form:
        Name = form["Name"].value
        Mid = form["Mid"].value
        cugradinterface.insertMinor(Name,Mid)

    elif "insertMinor" in form:
        cugradinterface.showInsertMinorForm()

    elif "insertStudentMajor" in form and "Sid" in form  and "Mid" in form:
        Sid = form["Sid"].value
        Mid = form["Mid"].value
        cugradinterface.insertStudentMajor(Sid,Mid)

    elif "insertStudentMajor" in form:
        cugradinterface.showInsertStudentMajorForm()

    elif "searchStudentInfo" in form and "Sid" in form:
        Sid = form["Sid"].value 
        cugradinterface.searchStudentInfo(Sid)

    # search for a name, and we DO NOT have the name
    elif "searchStudentInfo" in form:
        cugradinterface.showSearchStudentInfoForm()

        
    
    
    # default case: show menu
    else:        
        # substitute other functions in here to test from command line
        # cugradinterface.listArtists()
        
        # show the default page
        cugradinterface.showDefaultPage()

    #doHTMLTail()    





