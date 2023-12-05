val x = 1;
(*  x maps to 1 *)

fn f y = x + y;
(* f maps to a function that adds 1 to its argument *)

val x = 2;
(* x maps to 2 *)

val y = 3;
(* y maps to 3 *)

val z = f (x + y);
(* call the function defined on line 2 with 5 *)
(* in the end, z maps to 6 *)
