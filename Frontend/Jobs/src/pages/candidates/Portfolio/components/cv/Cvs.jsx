import React from 'react'
import pdfIcon from '../../../../../assets/icons/pdf.png'
import remove from '../../../../../assets/icons/eliminar.png'
import { useContext } from 'react'
import { authContext } from '../../../../../context/context'
import { BASE_URL_FILES } from '../../../../../constants/baseURL'

const Cvs = ({cv1, cv1_nombre, cv2, cv2_nombre, setEditableData, onHandleOpenModal, setIsEdited}) => {
  
    const { auth } = useContext(authContext)

    const handleRemovePdf = (e, target) => {
        setEditableData(data => ({...data, [target]: ""}))
        setIsEdited(true)
    }
    
    return (
        <div className='flex flex-col'>

        {
            (cv1 === null || cv2 === null) && (
                <div className='flex justify-center'>
                    {
                        auth.candidato_id &&
                        <button className='bg-eleventh w-full py-2' onClick={onHandleOpenModal}>
                            + Agregar Nuevo
                        </button>
                    }
                </div>
            )
        }
            {
                cv1 && (
                    <div className='w-full flex items-center justify-between shadow-md py-3 px-3 mt-4'>
                        <div className='flex items-center'>

                            <img src={pdfIcon} alt="" />
                            <p className='ml-2'>{cv1_nombre}</p>
                            <a href={`${BASE_URL_FILES}${cv1}`} 
                                target='blanck'
                                className='text-[12px] bg-fourth text-white h-5 rounded-lg px-2 ml-4'
                            >
                                Ver PDF
                            </a>
                        </div>
                        {
                            auth.candidato_id &&
                            <button> 
                                <img src={remove} onClick={(e) => handleRemovePdf(e, 'cv_1')} alt="" className='w-7' /> 
                            </button>
                        }
                    </div>
                )
            }

            {
                cv2 && (
                    <div className='w-full flex justify-between shadow-md py-3 px-3'>
                    <div className='flex items-center'>
                        <img src={pdfIcon} alt="" />
                        <p className='ml-2'>{cv2_nombre}</p>
                        <a href={`${BASE_URL_FILES}${cv2}`} 
                            target='blanck'
                            className='text-[12px] bg-fourth text-white h-5 rounded-lg px-2 ml-4'
                        >
                            Ver PDF
                        </a>
                    </div>
                    <button> <img src={remove} onClick={(e) => handleRemovePdf(e, 'cv_2')} alt="" className='w-7' /> </button>
                </div>
                )
            }
        </div>
  )
}

export default Cvs