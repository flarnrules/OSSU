;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname countdown-animation-starter-stripped) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

(define WIDTH 50)
(define HEIGHT 50)
(define CTR-X (/ WIDTH 2))
(define CTR-Y (/ HEIGHT 2))
(define MTS (empty-scene WIDTH HEIGHT))
(define TEXT-SIZE 24)
(define TEXT-COLOR "black")

(define (main cd)
  (big-bang cd
    (on-tick advance-countdown 1)
    (to-draw render-countdown)
    (on-key handle-key)))

(define (advance-countdown cd)
  (if (= 0 cd)
      0
      (- cd 1)))

(define (render-countdown cd)
  (place-image (text (number->string cd) TEXT-SIZE TEXT-COLOR)
               CTR-X CTR-Y
               MTS))

(define (handle-key cd ke)
  (cond [(key=? ke " ") 10]
        [else cd]))