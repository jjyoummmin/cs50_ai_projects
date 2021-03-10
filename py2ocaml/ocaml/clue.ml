open Logic

let mustard = Symbol("ColMustard")
let plum = Symbol("ProfPlum")
let scarlet = Symbol("MsScarlet")
let characters = [mustard; plum; scarlet]

let ballroom = Symbol("ballroom")
let kitchen = Symbol("kitchen")
let library = Symbol("library")
let rooms = [ballroom; kitchen; library]

let knife = Symbol("knife")
let revolver = Symbol("revolver")
let wrench = Symbol("wrench")
let weapons = [knife; revolver; wrench]

let symbols = characters @ rooms @ weapons    

let check_knowledge knowledge=
  let f s = 
    match model_check knowledge s with
    |true -> print_endline (Printer.sentence_to_str s^" : YES")      (* s가 범인인 것 확신 *)  
    |false -> match model_check knowledge (Not s) with 
             | true -> ()                                             (* s가 범인 아닌 것 확신 *) 
             | false ->print_endline (Printer.sentence_to_str s^" : MAYBE")
  in List.iter f symbols 

let k0 = And[
    Or[mustard; plum; scarlet];
    Or[ballroom; kitchen; library];
    Or[knife; revolver; wrench]] 

let k1 = add k0 ( And[Not(mustard); Not(kitchen); Not(revolver)] )
let k2 = add k1 ( Or[Not(scarlet); Not(library); Not(wrench)] )
let k3 = add k2 ( Not(plum) )    ;;
let k4 = add k3 ( Not(ballroom) ) in check_knowledge k4