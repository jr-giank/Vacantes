import React from 'react'
import { BASE_URL_FILES } from '../../../../../constants/baseURL'

const CandidatesAvailable_forTest_grid = ({candidate, setCurrenModalSection, setCurrentCandidate}) => {

  const handleAssignTest = (e) => {
    e.preventDefault()
    setCurrentCandidate(candidate)
    setCurrenModalSection(2)
  }
  
    return (
    <div className='flex items-center justify-between px-3 border-b border-fifth py-2'>
      <div className='flex items-center'>
        <img  src={`${BASE_URL_FILES}${candidate.foto}`} alt="" className='w-16 h-16 rounded-full' />
        <p className='ml-4 font-semibold'>{candidate.nombre} {candidate.apellido}</p>  
      </div>

      <button className='bg-seventh text-white px-1 py-1 text-[14px] rounded-md' onClick={handleAssignTest}>
        Asignar Prueba
      </button>

    </div>
  )
}

export default CandidatesAvailable_forTest_grid