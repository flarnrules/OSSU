(* helper functions to test out max functions *)

fun countup (from : int, to : int) =
    if from =to
    then to::[]
    else from :: countup(from+1, to);

fun countdown (from : int, to : int) =
    if from=to
    then to::[]
    else from :: countdown(from-1,to);
