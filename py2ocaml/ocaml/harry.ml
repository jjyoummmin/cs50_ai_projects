open Logic

let rain = Symbol("rain")
let hagrid = Symbol("hagrid")
let dumbledore = Symbol("dumbledore")

let knowledge = And [
    Implication(Not(rain), hagrid);
    Or[hagrid; dumbledore];
    Not(And[hagrid; dumbledore]);
    dumbledore] ;;

let main () = Printf.printf "%B\n" (model_check knowledge rain) in main ()