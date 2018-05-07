#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:24:00 2018

@author: Carolina
"""
import pymysql as db

class CUgradDB:
    def __init__( self):
      self.conn = db.connect(host = "localhost", user = "tnicolaantoniu", passwd = "tnicolaantoniu", db = "tnicolaantoniu_cugrad", use_unicode=True, charset="utf8")
      
    def __del__(self):
      self.conn.close()
    
    def listCourses(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM courses")

        # Demonstrates returning a cursor
        return(cur)

    def listMajors(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM majors")

        # Demonstrates returning a cursor
        return(cur)

    def listMinors(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM minors")

        # Demonstrates returning a cursor
        return(cur)

    def listStudents(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM students")

        # Demonstrates returning a cursor
        return(cur)

    def listPls(self):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM pls")
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)
    
        
    def searchCourses(self, dept):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (dept,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM courses WHERE Department like %s", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)

    def insertCourse(self, Name, Department, Level):
        cur = self.conn.cursor();
        params = (Name, Department, Level)
        cur.execute("INSERT INTO courses VALUES (%s,%s,%s)", params)
        self.conn.commit()

    def updatepls(self, name, plsid):
        cur = self.conn.cursor();
        params = (name, plsid)
        cur.execute("UPDATE pls SET Name=%s WHERE Id like %s",params)
        self.conn.commit()

    def deleteStudent(self, Sid):
        cur = self.conn.cursor();
        params = (Sid,)
        cur.execute("DELETE FROM students WHERE Id like %s",params)
        self.conn.commit()

    def findMissingPls(self, Sid):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (Sid,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT DISTINCT CP.PlsId FROM courses_for_pls AS CP WHERE CP.PlsId NOT IN (SELECT CP.PlsId FROM courses_for_pls AS CP,courses_taken AS CT WHERE CP.CourseDept = CT.CourseDept AND CP.CourseLevel = CT.CourseLevel AND CT.StudentId like %s)", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)

    def findNewCourses(self, Sid):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (Sid)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT C.Name,C.Department,C.Level FROM courses AS C WHERE (C.Department,C.Level) NOT IN (SELECT CT.CourseDept,CT.CourseLevel FROM courses_taken AS CT WHERE CT.StudentId like %s)", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)

    def deleteCourse(self, Department, Level):
        cur = self.conn.cursor();
        params = (Department, Level)
        cur.execute("DELETE FROM courses WHERE Department like %s AND Level like %s",params)
        self.conn.commit()

    def insertStudent(self, Lname, Fname, Sid, Username, GradSemester):
        cur = self.conn.cursor();
        params = (Lname, Fname, Sid, Username, GradSemester)
        cur.execute("INSERT INTO students VALUES (%s,%s,%s,%s,%s)", params)
        self.conn.commit()

    def findIncompleteMajor(self, Sid):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (Sid, Sid)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT R.CourseDept, R.CourseLevel FROM required_for_major as R, majors_in as M, courses_taken as CT WHERE M.MajorId = R.MajorId AND M.StudentId like %s AND (R.CourseDept, R.CourseLevel) NOT IN (SELECT CT.CourseDept, CT.CourseLevel FROM courses_taken AS CT, majors_in as M WHERE CT.StudentId like %s) GROUP BY R.CourseDept, R.CourseLevel;", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)

    def insertMajor(self, Name, Mid):
        cur = self.conn.cursor();
        params = (Name, Mid)
        cur.execute("INSERT INTO majors VALUES (%s,%s)", params)
        self.conn.commit()

    def insertMinor(self, Name, Mid):
        cur = self.conn.cursor();
        params = (Name, Mid)
        cur.execute("INSERT INTO minors VALUES (%s,%s)", params)
        self.conn.commit()

    def insertStudentMajor(self, Sid, Mid):
        cur = self.conn.cursor();
        params = (Sid, Mid)
        cur.execute("INSERT INTO majors_in VALUES (%s,%s)", params)
        self.conn.commit()

    def searchStudentInfo(self, Sid):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (Sid,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT S.Fname, S.Lname, S.Id, S.GradSemester, GROUP_CONCAT(M.MajorId), GROUP_CONCAT(Mi.MinorId) FROM students as S, majors_in as M, minors_in as Mi WHERE S.Id like %s AND S.Id = M.StudentId AND S.Id = Mi.StudentId GROUP BY S.Id", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)




        
      
        
