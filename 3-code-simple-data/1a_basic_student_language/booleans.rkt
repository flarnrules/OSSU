;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname booleans) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;true
;false

(define WIDTH 100)
(define HEIGHT 100)

(string=? "foo" "bar")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

(define (I3 s)
  (rectangle 10 20 "solid" s))

(I3 "blue")
  
(rectangle 10 20 "solid" "red")

(< (image-width I1)
   (image-width I2))

(I3 "green")