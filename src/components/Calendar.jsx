import * as React from 'react';
import Paper from '@mui/material/Paper';
import {
  Scheduler,
  WeekView,
  Appointments,
  AppointmentTooltip,
  AppointmentForm,
} from '@devexpress/dx-react-scheduler-material-ui';

const appointments = [
  {
    title: 'Inteligencia Artificial',
    startDate: new Date(2023, 3, 24, 10),
    endDate: new Date(2023, 3, 24, 12),
    id: 0,
    location: 'Room 1',
  }, {
    title: 'Inteligencia Artificial',
    startDate: new Date(2023, 3, 28, 10),
    endDate: new Date(2023, 3, 28, 12),
    id: 1,
    location: 'Room 1',
  }, {
    title: 'Proyecto Integrador',
    startDate: new Date(2023, 3, 29, 8),
    endDate: new Date(2023, 3, 29, 12),
    id: 2,
    location: 'Room 2',
  }, {
    title: 'Analisis y Diseño de Algoritmos II',
    startDate: new Date(2023, 3, 25, 15, 0),
    endDate: new Date(2023, 3, 25, 16, 30),
    id: 3,
    location: 'Room 2',
  }, {
    title: 'Analisis y Diseño de Algoritmos II',
    startDate: new Date(2023, 3, 27, 7, 0),
    endDate: new Date(2023, 3, 27, 8, 30),
    id: 4,
    location: 'Room 2',
  }, {
    title: 'Infraestructuras Paralelas y Distribuidas',
    startDate: new Date(2023, 3, 25, 9, 0),
    endDate: new Date(2023, 3, 25, 12, 0),
    id: 5,
    location: 'Room 2',
  }, {
    title: 'Desarrollo de Software II',
    startDate: new Date(2023, 3, 28, 17, 0),
    endDate: new Date(2023, 3, 28, 20, 0),
    id: 6,
    location: 'Room 2',
  },
];


const Calendar = () => {

    return (
      <Paper>
        <Scheduler
          data={appointments}
          height={600}
        >
          <WeekView
            startDayHour={7}
            endDayHour={22}
          />

          <Appointments />
          <AppointmentTooltip
            showCloseButton
            showOpenButton
          />
          <AppointmentForm
            readOnly
          />
        </Scheduler>
      </Paper>
    );
  }

export default Calendar;