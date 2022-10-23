import validator from "validator";

export const validateCandidatesRegistrationForm = (name, value) => {
    switch(name){
        case "name":
            if(value === ""){
                return  "El nombre es requerido"
            }
            break;

        case "lastName":
            if(value === ""){
                return  "El apellido es requerido"
            }
            break;

        case "email":
            if(value === ""){
                return "El email es requerido"
            }
            if(!validator.isEmail(value)){
                return "Este email es inválido"
            }
            break;

        case "password":
            if(value.length < 7){
                return "La contraseña debe tener al menos 7 caracteeres"
            }
            break;

        case "phoneNumber":
            if(value !== "" && !validator.isMobilePhone(value)){
                return "El número de teléfono proporcionado no es válido"
            }
            break;

        case "pais":
            if(value === ""){
                return "Se requiere seleccionar el país"
            }
            break;

        case "birthday":
            if(value === ""){
                return "Agregue una su fecha de nacimiento"
            }
            break;

        case "ocupation":
            if(value === ""){
                return "Agregue su ocupacion"
            }
            break;
    }
    return null
}