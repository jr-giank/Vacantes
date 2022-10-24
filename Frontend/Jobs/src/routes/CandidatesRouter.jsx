import React from 'react'

import {Routes, Route } from 'react-router-dom'

import VacancyViewSingle from '../pages/candidates/Single Vacancy View/VacancyViewSingle'
import VacancyViewAll from '../pages/candidates/All Vacancy View/VacancyViewAll'

const CandidatesRouter = () => {
  return (
    <Routes>
        <Route path='/viewAllVacancies' element={<VacancyViewAll />} />
        <Route path='/viewSingleVacancy/:id' element={<VacancyViewSingle />} />
        <Route path='/candidates/signUp' element={<CandidatesRegistrationPage />} />
        <Route path='/candidates/viewSaveVacancies' element={<VacanciesSavePage />} />
    </Routes>
  )
}

export default CandidatesRouter