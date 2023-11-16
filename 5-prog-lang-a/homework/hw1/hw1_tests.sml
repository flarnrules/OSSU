(* tests for hw1 *)

(* create an assert equal function *)
fun assertEqual (actual, expected, message) =
    if actual = expected then
	print("Test passed: " ^ message ^ "\n")
    else
	print("Test failed: " ^ message ^ "; expected: " ^ Int.toString expected ^ ", but got " ^ Int.toString actual ^ "/n");

(* test functions *)

(* 1 - number_in_month *)
fun test_number_in_month () =
    let
	(* example date list *)
	val dates = [(2023, 1, 15), (2025, 12, 30), (2016, 6, 18), (2023, 6, 30)]
			val _ = assertEqual (number_in_month (dates, 1) 2, 
