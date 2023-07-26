;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname circles) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;"apple"
;"Ada"
;(string-append "Ada" " " "Lovelace")

;(string-length "apple")
;(substring "Caribou" 2 4)
;(substring "012345678" 2 4)
;(substring "Caribou" 0 3)

(above (circle 10 "solid" "red")
       (circle 20 "solid" "blue")
       (circle 30 "solid" "green"))

(beside (circle 10 "solid" "red")
        (circle 20 "solid" "blue")
        (circle 30 "solid" "green"))

(overlay (circle 10 "solid" "red")
         (circle 20 "solid" "blue")
         (circle 30 "solid" "green")
         (circle 50 "outline" "orange")
         (circle 60 "outline" "orange")
         (circle 70 "outline" "orange"))