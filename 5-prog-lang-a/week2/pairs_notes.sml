(* from page 6 of week2 notes *)
(* we are learning about pairs and functions of pairs *)

val pr = (5, true)
val pr1 = (10, 10)
val pr2 = (5, 5)
val x = 12
val y = 30
	      
fun swap (pr : int*bool) = (* see the type t1*t2 *)
    (#2 pr, #1 pr)

fun sum_two_pairs (pr1 : int*int, pr2 : int*int) =
    (#1 pr1) + (#2 pr1) + (#1 pr2) + (#2 pr2)

fun div_mod (x : int, y : int) =
    (x div y, x mod y)

fun sort_pair (pr : int*int) =
    if (#1 pr) < (#2 pr)
    then pr
    else ((#2 pr),(#1 pr))


