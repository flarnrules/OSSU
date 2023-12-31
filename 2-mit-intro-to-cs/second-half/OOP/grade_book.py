#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:39:04 2023

@author: flarnrules
"""

class Grades(object):
	"""A mapping from students to a list of grades"""
	def __init__(self):
		"""Create empty grade book"""
		self.students = []
		self. grades = {}
		self.isSorted = True

	def addStudent(self, student):
		"""Assumes: student is of type Student
		Add student to the grade book"""
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False

	def addGrade(self, student, grade):
		"""Assumes: grade is a float
		Add grade to the list of grades for student"""
		try:
			self.grades[student.getIdNum()].append(grade)
		except KeyError:
			raise ValueError('Student not in grade book')

	def getGrades(self, student):
		"""Return a list of grades for a student"""
		try:
			return self.grades[student.getIdNum()][:]
		except KeyError:
			raise ValueError('Student not in gradebook')

	def allStudents(self):
		"""return a list of the students in the gb"""
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		return self.students[:]

	def gradeReport(course):
		"""Assumes: course is of type grades"""
		report = []
		for s in course.allStudents():
			tot = 0.0
			numGrades = 0
			for g in course.getGrades(s):
				tot += g
				numGrades += 1
			try:
				average = tot / numGrades
				report.append(str(s) + '\'s mean grade is ' + str(average))
			except ZeroDivisionError:
				report.append(str(s) + ' has no grades')
		return '\n'.join(report)

