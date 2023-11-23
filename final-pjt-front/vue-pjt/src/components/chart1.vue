<template>
    <div style="text-align: center;">{{ day }}개월 목표기간 금리에 따른 그래프</div>
    <Bar :data="chartData" :options="chartOptions" />
  </template>
  <script>
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
  props: ['name1', 'data3', 'data4', 'day'],
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: this.name1,
        datasets: [
          {
            label: '저축 금리',
            backgroundColor: '#f87979',
            data: this.data3,
          },
          {
            label: '남은 목표금액',
            backgroundColor: 'rgba(255, 206, 86, 1)',
            data: this.data4,
          },
        ],
      },
      chartOptions: {
        scales: {
          x: {
            ticks: {
              maxRotation: 45, // Adjust the rotation angle as needed
              minRotation: 45,
            },
          },
        },
      },
    };
  },
};
  </script>