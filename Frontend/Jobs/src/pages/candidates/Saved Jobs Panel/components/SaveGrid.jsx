import React, { useContext } from 'react'
import { Link } from 'react-router-dom'
import { authContext } from '../../../../context/context'
import { f_delete } from '../../../../services/services'
import { BASE_URL_FILES } from '../../../../constants/baseURL'

const SaveGrid = ({vacancy, setVacancies}) => {

   const { auth } = useContext(authContext) 

   const onHandleRemove = (e) => {
        e.preventDefault()
        f_delete(`vacante/guardada/eliminar/${auth.user_id}/${vacancy.vacante.id}/`, {"Authorization":`Bearer ${auth.token}`})
        .then(data => {
            if(data.exito){
                setVacancies(vacancies => vacancies.filter(vac => vac.id !== vacancy.id))
            }else{
                alert("Error al eliminar vacante guardada. Intente nuevamente")
            }
        })
   }

  return (

    <div className='border-b w-full border-fifth pl-4 pr-4 py-4 '>

        <div className='flex gap-4'>
            <img className='w-16 h-16 rounded-full 'src={`${BASE_URL_FILES}${vacancy.vacante.empresa.foto}`} alt="Scopic Software" />
        
            <div className='flex flex-col'>
                <h4 className='font-bold'>{vacancy.vacante.nombre_puesto}               
                    <span className='border-solid border-2 border-nineth rounded bg-nineth m-2 text-sm'>jornada completa</span>
                    <span className='border-solid border-2 border-nineth rounded bg-nineth m-2 text-sm'>remoto</span>
                </h4>
                <div>
                    <Link className='justify-center text-[12px] border border-sixth rounded-lg cursor-pointer mr-3 mt-5 py-2 px-4 hover:bg-secondary ' to= {`/app/candidate/viewSingleVacancy/${vacancy.vacante.id}`} >Ver vacante</Link> 
                    <button className='justify-center cursor-pointer text-[12px] mt-5 py-1.5 rounded-lg px-4 hover:bg-tertiary border border-sixth' onClick={onHandleRemove}>Dejar de guardar</button>  

                </div>
            </div>
        </div>
    </div>
  )
}

export default SaveGrid