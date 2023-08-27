;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname count-down) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Data Definitions

;; Count is Number
;; interp. number in countdown sequence


;; Function Definitions


;; count-down
;; Natural -> Natural
;; Decrements number by one
(check-expect (count-down 1) 0)
(check-expect (count-down 0) 0)
(check-expect (count-down 10) 9)

(define (count-down c)
  (- c SPEED))

;; 
