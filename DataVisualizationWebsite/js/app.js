/**
 * PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB & SEABORN
 * Senior Full-Stack Analytics Application Logic
 * Interactive Plotly.js charts, responsive data table, and real-time statistics.
 */

// Embedded authentic Seaborn tips dataset (244 records)
const EMBEDDED_TIPS_DATA = [
  {
    "total_bill": 16.99,
    "tip": 1.01,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 1,
    "tip_pct": 5.94
  },
  {
    "total_bill": 10.34,
    "tip": 1.66,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 2,
    "tip_pct": 16.05
  },
  {
    "total_bill": 21.01,
    "tip": 3.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 3,
    "tip_pct": 16.66
  },
  {
    "total_bill": 23.68,
    "tip": 3.31,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 4,
    "tip_pct": 13.98
  },
  {
    "total_bill": 24.59,
    "tip": 3.61,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 5,
    "tip_pct": 14.68
  },
  {
    "total_bill": 25.29,
    "tip": 4.71,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 6,
    "tip_pct": 18.62
  },
  {
    "total_bill": 8.77,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 7,
    "tip_pct": 22.81
  },
  {
    "total_bill": 26.88,
    "tip": 3.12,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 8,
    "tip_pct": 11.61
  },
  {
    "total_bill": 15.04,
    "tip": 1.96,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 9,
    "tip_pct": 13.03
  },
  {
    "total_bill": 14.78,
    "tip": 3.23,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 10,
    "tip_pct": 21.85
  },
  {
    "total_bill": 10.27,
    "tip": 1.71,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 11,
    "tip_pct": 16.65
  },
  {
    "total_bill": 35.26,
    "tip": 5.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 12,
    "tip_pct": 14.18
  },
  {
    "total_bill": 15.42,
    "tip": 1.57,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 13,
    "tip_pct": 10.18
  },
  {
    "total_bill": 18.43,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 14,
    "tip_pct": 16.28
  },
  {
    "total_bill": 14.83,
    "tip": 3.02,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 15,
    "tip_pct": 20.36
  },
  {
    "total_bill": 21.58,
    "tip": 3.92,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 16,
    "tip_pct": 18.16
  },
  {
    "total_bill": 10.33,
    "tip": 1.67,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 17,
    "tip_pct": 16.17
  },
  {
    "total_bill": 16.29,
    "tip": 3.71,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 18,
    "tip_pct": 22.77
  },
  {
    "total_bill": 16.97,
    "tip": 3.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 19,
    "tip_pct": 20.62
  },
  {
    "total_bill": 20.65,
    "tip": 3.35,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 20,
    "tip_pct": 16.22
  },
  {
    "total_bill": 17.92,
    "tip": 4.08,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 21,
    "tip_pct": 22.77
  },
  {
    "total_bill": 20.29,
    "tip": 2.75,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 22,
    "tip_pct": 13.55
  },
  {
    "total_bill": 15.77,
    "tip": 2.23,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 23,
    "tip_pct": 14.14
  },
  {
    "total_bill": 39.42,
    "tip": 7.58,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 24,
    "tip_pct": 19.23
  },
  {
    "total_bill": 19.82,
    "tip": 3.18,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 25,
    "tip_pct": 16.04
  },
  {
    "total_bill": 17.81,
    "tip": 2.34,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 26,
    "tip_pct": 13.14
  },
  {
    "total_bill": 13.37,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 27,
    "tip_pct": 14.96
  },
  {
    "total_bill": 12.69,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 28,
    "tip_pct": 15.76
  },
  {
    "total_bill": 21.7,
    "tip": 4.3,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 29,
    "tip_pct": 19.82
  },
  {
    "total_bill": 19.65,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 30,
    "tip_pct": 15.27
  },
  {
    "total_bill": 9.55,
    "tip": 1.45,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 31,
    "tip_pct": 15.18
  },
  {
    "total_bill": 18.35,
    "tip": 2.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 32,
    "tip_pct": 13.62
  },
  {
    "total_bill": 15.06,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 33,
    "tip_pct": 19.92
  },
  {
    "total_bill": 20.69,
    "tip": 2.45,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 34,
    "tip_pct": 11.84
  },
  {
    "total_bill": 17.78,
    "tip": 3.27,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 35,
    "tip_pct": 18.39
  },
  {
    "total_bill": 24.06,
    "tip": 3.6,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 36,
    "tip_pct": 14.96
  },
  {
    "total_bill": 16.31,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 37,
    "tip_pct": 12.26
  },
  {
    "total_bill": 16.93,
    "tip": 3.07,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 38,
    "tip_pct": 18.13
  },
  {
    "total_bill": 18.69,
    "tip": 2.31,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 39,
    "tip_pct": 12.36
  },
  {
    "total_bill": 31.27,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 40,
    "tip_pct": 15.99
  },
  {
    "total_bill": 16.04,
    "tip": 2.24,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 41,
    "tip_pct": 13.97
  },
  {
    "total_bill": 17.46,
    "tip": 2.54,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 42,
    "tip_pct": 14.55
  },
  {
    "total_bill": 13.94,
    "tip": 3.06,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 43,
    "tip_pct": 21.95
  },
  {
    "total_bill": 9.68,
    "tip": 1.32,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 44,
    "tip_pct": 13.64
  },
  {
    "total_bill": 30.4,
    "tip": 5.6,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 45,
    "tip_pct": 18.42
  },
  {
    "total_bill": 18.29,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 46,
    "tip_pct": 16.4
  },
  {
    "total_bill": 22.23,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 47,
    "tip_pct": 22.49
  },
  {
    "total_bill": 32.4,
    "tip": 6.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 48,
    "tip_pct": 18.52
  },
  {
    "total_bill": 28.55,
    "tip": 2.05,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 49,
    "tip_pct": 7.18
  },
  {
    "total_bill": 18.04,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 50,
    "tip_pct": 16.63
  },
  {
    "total_bill": 12.54,
    "tip": 2.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 51,
    "tip_pct": 19.94
  },
  {
    "total_bill": 10.29,
    "tip": 2.6,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 52,
    "tip_pct": 25.27
  },
  {
    "total_bill": 34.81,
    "tip": 5.2,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 53,
    "tip_pct": 14.94
  },
  {
    "total_bill": 9.94,
    "tip": 1.56,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 54,
    "tip_pct": 15.69
  },
  {
    "total_bill": 25.56,
    "tip": 4.34,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 55,
    "tip_pct": 16.98
  },
  {
    "total_bill": 19.49,
    "tip": 3.51,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 56,
    "tip_pct": 18.01
  },
  {
    "total_bill": 38.01,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 57,
    "tip_pct": 7.89
  },
  {
    "total_bill": 26.41,
    "tip": 1.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 58,
    "tip_pct": 5.68
  },
  {
    "total_bill": 11.24,
    "tip": 1.76,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 59,
    "tip_pct": 15.66
  },
  {
    "total_bill": 48.27,
    "tip": 6.73,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 60,
    "tip_pct": 13.94
  },
  {
    "total_bill": 20.29,
    "tip": 3.21,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 61,
    "tip_pct": 15.82
  },
  {
    "total_bill": 13.81,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 62,
    "tip_pct": 14.48
  },
  {
    "total_bill": 11.02,
    "tip": 1.98,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 63,
    "tip_pct": 17.97
  },
  {
    "total_bill": 18.29,
    "tip": 3.76,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 64,
    "tip_pct": 20.56
  },
  {
    "total_bill": 17.59,
    "tip": 2.64,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 65,
    "tip_pct": 15.01
  },
  {
    "total_bill": 20.08,
    "tip": 3.15,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 66,
    "tip_pct": 15.69
  },
  {
    "total_bill": 16.45,
    "tip": 2.47,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 67,
    "tip_pct": 15.02
  },
  {
    "total_bill": 3.07,
    "tip": 1.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 1,
    "id": 68,
    "tip_pct": 32.57
  },
  {
    "total_bill": 20.23,
    "tip": 2.01,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 69,
    "tip_pct": 9.94
  },
  {
    "total_bill": 15.01,
    "tip": 2.09,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 70,
    "tip_pct": 13.92
  },
  {
    "total_bill": 12.02,
    "tip": 1.97,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 71,
    "tip_pct": 16.39
  },
  {
    "total_bill": 17.07,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 72,
    "tip_pct": 17.57
  },
  {
    "total_bill": 26.86,
    "tip": 3.14,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 73,
    "tip_pct": 11.69
  },
  {
    "total_bill": 25.28,
    "tip": 5.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 74,
    "tip_pct": 19.78
  },
  {
    "total_bill": 14.73,
    "tip": 2.2,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 75,
    "tip_pct": 14.94
  },
  {
    "total_bill": 10.51,
    "tip": 1.25,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 76,
    "tip_pct": 11.89
  },
  {
    "total_bill": 17.92,
    "tip": 3.08,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 77,
    "tip_pct": 17.19
  },
  {
    "total_bill": 27.2,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 4,
    "id": 78,
    "tip_pct": 14.71
  },
  {
    "total_bill": 22.76,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 79,
    "tip_pct": 13.18
  },
  {
    "total_bill": 17.29,
    "tip": 2.71,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 80,
    "tip_pct": 15.67
  },
  {
    "total_bill": 19.44,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 81,
    "tip_pct": 15.43
  },
  {
    "total_bill": 16.66,
    "tip": 3.4,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 82,
    "tip_pct": 20.41
  },
  {
    "total_bill": 10.07,
    "tip": 1.83,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 1,
    "id": 83,
    "tip_pct": 18.17
  },
  {
    "total_bill": 32.68,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 84,
    "tip_pct": 15.3
  },
  {
    "total_bill": 15.98,
    "tip": 2.03,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 85,
    "tip_pct": 12.7
  },
  {
    "total_bill": 34.83,
    "tip": 5.17,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 4,
    "id": 86,
    "tip_pct": 14.84
  },
  {
    "total_bill": 13.03,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 87,
    "tip_pct": 15.35
  },
  {
    "total_bill": 18.28,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 88,
    "tip_pct": 21.88
  },
  {
    "total_bill": 24.71,
    "tip": 5.85,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 89,
    "tip_pct": 23.67
  },
  {
    "total_bill": 21.16,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 90,
    "tip_pct": 14.18
  },
  {
    "total_bill": 28.97,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 91,
    "tip_pct": 10.36
  },
  {
    "total_bill": 22.49,
    "tip": 3.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 92,
    "tip_pct": 15.56
  },
  {
    "total_bill": 5.75,
    "tip": 1.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 93,
    "tip_pct": 17.39
  },
  {
    "total_bill": 16.32,
    "tip": 4.3,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 94,
    "tip_pct": 26.35
  },
  {
    "total_bill": 22.75,
    "tip": 3.25,
    "sex": "Female",
    "smoker": "No",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 95,
    "tip_pct": 14.29
  },
  {
    "total_bill": 40.17,
    "tip": 4.73,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 4,
    "id": 96,
    "tip_pct": 11.77
  },
  {
    "total_bill": 27.28,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 97,
    "tip_pct": 14.66
  },
  {
    "total_bill": 12.03,
    "tip": 1.5,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 98,
    "tip_pct": 12.47
  },
  {
    "total_bill": 21.01,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 99,
    "tip_pct": 14.28
  },
  {
    "total_bill": 12.46,
    "tip": 1.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 100,
    "tip_pct": 12.04
  },
  {
    "total_bill": 11.35,
    "tip": 2.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 101,
    "tip_pct": 22.03
  },
  {
    "total_bill": 15.38,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Dinner",
    "size": 2,
    "id": 102,
    "tip_pct": 19.51
  },
  {
    "total_bill": 44.3,
    "tip": 2.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 103,
    "tip_pct": 5.64
  },
  {
    "total_bill": 22.42,
    "tip": 3.48,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 104,
    "tip_pct": 15.52
  },
  {
    "total_bill": 20.92,
    "tip": 4.08,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 105,
    "tip_pct": 19.5
  },
  {
    "total_bill": 15.36,
    "tip": 1.64,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 106,
    "tip_pct": 10.68
  },
  {
    "total_bill": 20.49,
    "tip": 4.06,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 107,
    "tip_pct": 19.81
  },
  {
    "total_bill": 25.21,
    "tip": 4.29,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 108,
    "tip_pct": 17.02
  },
  {
    "total_bill": 18.24,
    "tip": 3.76,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 109,
    "tip_pct": 20.61
  },
  {
    "total_bill": 14.31,
    "tip": 4.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 110,
    "tip_pct": 27.95
  },
  {
    "total_bill": 14.0,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 111,
    "tip_pct": 21.43
  },
  {
    "total_bill": 7.25,
    "tip": 1.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 1,
    "id": 112,
    "tip_pct": 13.79
  },
  {
    "total_bill": 38.07,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 113,
    "tip_pct": 10.51
  },
  {
    "total_bill": 23.95,
    "tip": 2.55,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 114,
    "tip_pct": 10.65
  },
  {
    "total_bill": 25.71,
    "tip": 4.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 115,
    "tip_pct": 15.56
  },
  {
    "total_bill": 17.31,
    "tip": 3.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 116,
    "tip_pct": 20.22
  },
  {
    "total_bill": 29.93,
    "tip": 5.07,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 117,
    "tip_pct": 16.94
  },
  {
    "total_bill": 10.65,
    "tip": 1.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 118,
    "tip_pct": 14.08
  },
  {
    "total_bill": 12.43,
    "tip": 1.8,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 119,
    "tip_pct": 14.48
  },
  {
    "total_bill": 24.08,
    "tip": 2.92,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 4,
    "id": 120,
    "tip_pct": 12.13
  },
  {
    "total_bill": 11.69,
    "tip": 2.31,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 121,
    "tip_pct": 19.76
  },
  {
    "total_bill": 13.42,
    "tip": 1.68,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 122,
    "tip_pct": 12.52
  },
  {
    "total_bill": 14.26,
    "tip": 2.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 123,
    "tip_pct": 17.53
  },
  {
    "total_bill": 15.95,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 124,
    "tip_pct": 12.54
  },
  {
    "total_bill": 12.48,
    "tip": 2.52,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 125,
    "tip_pct": 20.19
  },
  {
    "total_bill": 29.8,
    "tip": 4.2,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 6,
    "id": 126,
    "tip_pct": 14.09
  },
  {
    "total_bill": 8.52,
    "tip": 1.48,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 127,
    "tip_pct": 17.37
  },
  {
    "total_bill": 14.52,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 128,
    "tip_pct": 13.77
  },
  {
    "total_bill": 11.38,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 129,
    "tip_pct": 17.57
  },
  {
    "total_bill": 22.82,
    "tip": 2.18,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 3,
    "id": 130,
    "tip_pct": 9.55
  },
  {
    "total_bill": 19.08,
    "tip": 1.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 131,
    "tip_pct": 7.86
  },
  {
    "total_bill": 20.27,
    "tip": 2.83,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 132,
    "tip_pct": 13.96
  },
  {
    "total_bill": 11.17,
    "tip": 1.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 133,
    "tip_pct": 13.43
  },
  {
    "total_bill": 12.26,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 134,
    "tip_pct": 16.31
  },
  {
    "total_bill": 18.26,
    "tip": 3.25,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 135,
    "tip_pct": 17.8
  },
  {
    "total_bill": 8.51,
    "tip": 1.25,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 136,
    "tip_pct": 14.69
  },
  {
    "total_bill": 10.33,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 137,
    "tip_pct": 19.36
  },
  {
    "total_bill": 14.15,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 138,
    "tip_pct": 14.13
  },
  {
    "total_bill": 16.0,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 139,
    "tip_pct": 12.5
  },
  {
    "total_bill": 13.16,
    "tip": 2.75,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 140,
    "tip_pct": 20.9
  },
  {
    "total_bill": 17.47,
    "tip": 3.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 141,
    "tip_pct": 20.03
  },
  {
    "total_bill": 34.3,
    "tip": 6.7,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 6,
    "id": 142,
    "tip_pct": 19.53
  },
  {
    "total_bill": 41.19,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 5,
    "id": 143,
    "tip_pct": 12.14
  },
  {
    "total_bill": 27.05,
    "tip": 5.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 6,
    "id": 144,
    "tip_pct": 18.48
  },
  {
    "total_bill": 16.43,
    "tip": 2.3,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 145,
    "tip_pct": 14.0
  },
  {
    "total_bill": 8.35,
    "tip": 1.5,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 146,
    "tip_pct": 17.96
  },
  {
    "total_bill": 18.64,
    "tip": 1.36,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 3,
    "id": 147,
    "tip_pct": 7.3
  },
  {
    "total_bill": 11.87,
    "tip": 1.63,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 148,
    "tip_pct": 13.73
  },
  {
    "total_bill": 9.78,
    "tip": 1.73,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 149,
    "tip_pct": 17.69
  },
  {
    "total_bill": 7.51,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 150,
    "tip_pct": 26.63
  },
  {
    "total_bill": 14.07,
    "tip": 2.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 151,
    "tip_pct": 17.77
  },
  {
    "total_bill": 13.13,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 152,
    "tip_pct": 15.23
  },
  {
    "total_bill": 17.26,
    "tip": 2.74,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 153,
    "tip_pct": 15.87
  },
  {
    "total_bill": 24.55,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 154,
    "tip_pct": 8.15
  },
  {
    "total_bill": 19.77,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 155,
    "tip_pct": 10.12
  },
  {
    "total_bill": 29.85,
    "tip": 5.14,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 5,
    "id": 156,
    "tip_pct": 17.22
  },
  {
    "total_bill": 48.17,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 6,
    "id": 157,
    "tip_pct": 10.38
  },
  {
    "total_bill": 25.0,
    "tip": 3.75,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 158,
    "tip_pct": 15.0
  },
  {
    "total_bill": 13.39,
    "tip": 2.61,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 159,
    "tip_pct": 19.49
  },
  {
    "total_bill": 16.49,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 160,
    "tip_pct": 12.13
  },
  {
    "total_bill": 21.5,
    "tip": 3.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 161,
    "tip_pct": 16.28
  },
  {
    "total_bill": 12.66,
    "tip": 2.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 162,
    "tip_pct": 19.75
  },
  {
    "total_bill": 16.21,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 163,
    "tip_pct": 12.34
  },
  {
    "total_bill": 13.81,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 164,
    "tip_pct": 14.48
  },
  {
    "total_bill": 17.51,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 165,
    "tip_pct": 17.13
  },
  {
    "total_bill": 24.52,
    "tip": 3.48,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 166,
    "tip_pct": 14.19
  },
  {
    "total_bill": 20.76,
    "tip": 2.24,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 167,
    "tip_pct": 10.79
  },
  {
    "total_bill": 31.71,
    "tip": 4.5,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 168,
    "tip_pct": 14.19
  },
  {
    "total_bill": 10.59,
    "tip": 1.61,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 169,
    "tip_pct": 15.2
  },
  {
    "total_bill": 10.63,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 170,
    "tip_pct": 18.81
  },
  {
    "total_bill": 50.81,
    "tip": 10.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 171,
    "tip_pct": 19.68
  },
  {
    "total_bill": 15.81,
    "tip": 3.16,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 172,
    "tip_pct": 19.99
  },
  {
    "total_bill": 7.25,
    "tip": 5.15,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 173,
    "tip_pct": 71.03
  },
  {
    "total_bill": 31.85,
    "tip": 3.18,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 174,
    "tip_pct": 9.98
  },
  {
    "total_bill": 16.82,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 175,
    "tip_pct": 23.78
  },
  {
    "total_bill": 32.9,
    "tip": 3.11,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 176,
    "tip_pct": 9.45
  },
  {
    "total_bill": 17.89,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 177,
    "tip_pct": 11.18
  },
  {
    "total_bill": 14.48,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 178,
    "tip_pct": 13.81
  },
  {
    "total_bill": 9.6,
    "tip": 4.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 179,
    "tip_pct": 41.67
  },
  {
    "total_bill": 34.63,
    "tip": 3.55,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 180,
    "tip_pct": 10.25
  },
  {
    "total_bill": 34.65,
    "tip": 3.68,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 181,
    "tip_pct": 10.62
  },
  {
    "total_bill": 23.33,
    "tip": 5.65,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 182,
    "tip_pct": 24.22
  },
  {
    "total_bill": 45.35,
    "tip": 3.5,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 183,
    "tip_pct": 7.72
  },
  {
    "total_bill": 23.17,
    "tip": 6.5,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 4,
    "id": 184,
    "tip_pct": 28.05
  },
  {
    "total_bill": 40.55,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 185,
    "tip_pct": 7.4
  },
  {
    "total_bill": 20.69,
    "tip": 5.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sun",
    "time": "Dinner",
    "size": 5,
    "id": 186,
    "tip_pct": 24.17
  },
  {
    "total_bill": 20.9,
    "tip": 3.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 187,
    "tip_pct": 16.75
  },
  {
    "total_bill": 30.46,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 5,
    "id": 188,
    "tip_pct": 6.57
  },
  {
    "total_bill": 18.15,
    "tip": 3.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 189,
    "tip_pct": 19.28
  },
  {
    "total_bill": 23.1,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 3,
    "id": 190,
    "tip_pct": 17.32
  },
  {
    "total_bill": 15.69,
    "tip": 1.5,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sun",
    "time": "Dinner",
    "size": 2,
    "id": 191,
    "tip_pct": 9.56
  },
  {
    "total_bill": 19.81,
    "tip": 4.19,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 192,
    "tip_pct": 21.15
  },
  {
    "total_bill": 28.44,
    "tip": 2.56,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 193,
    "tip_pct": 9.0
  },
  {
    "total_bill": 15.48,
    "tip": 2.02,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 194,
    "tip_pct": 13.05
  },
  {
    "total_bill": 16.58,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 195,
    "tip_pct": 24.13
  },
  {
    "total_bill": 7.56,
    "tip": 1.44,
    "sex": "Male",
    "smoker": "No",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 196,
    "tip_pct": 19.05
  },
  {
    "total_bill": 10.34,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 197,
    "tip_pct": 19.34
  },
  {
    "total_bill": 43.11,
    "tip": 5.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 4,
    "id": 198,
    "tip_pct": 11.6
  },
  {
    "total_bill": 13.0,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 199,
    "tip_pct": 15.38
  },
  {
    "total_bill": 13.51,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 200,
    "tip_pct": 14.8
  },
  {
    "total_bill": 18.71,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 3,
    "id": 201,
    "tip_pct": 21.38
  },
  {
    "total_bill": 12.74,
    "tip": 2.01,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 202,
    "tip_pct": 15.78
  },
  {
    "total_bill": 13.0,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 203,
    "tip_pct": 15.38
  },
  {
    "total_bill": 16.4,
    "tip": 2.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 2,
    "id": 204,
    "tip_pct": 15.24
  },
  {
    "total_bill": 20.53,
    "tip": 4.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 4,
    "id": 205,
    "tip_pct": 19.48
  },
  {
    "total_bill": 16.47,
    "tip": 3.23,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Thur",
    "time": "Lunch",
    "size": 3,
    "id": 206,
    "tip_pct": 19.61
  },
  {
    "total_bill": 26.59,
    "tip": 3.41,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 207,
    "tip_pct": 12.82
  },
  {
    "total_bill": 38.73,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 208,
    "tip_pct": 7.75
  },
  {
    "total_bill": 24.27,
    "tip": 2.03,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 209,
    "tip_pct": 8.36
  },
  {
    "total_bill": 12.76,
    "tip": 2.23,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 210,
    "tip_pct": 17.48
  },
  {
    "total_bill": 30.06,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 211,
    "tip_pct": 6.65
  },
  {
    "total_bill": 25.89,
    "tip": 5.16,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 212,
    "tip_pct": 19.93
  },
  {
    "total_bill": 48.33,
    "tip": 9.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 213,
    "tip_pct": 18.62
  },
  {
    "total_bill": 13.27,
    "tip": 2.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 214,
    "tip_pct": 18.84
  },
  {
    "total_bill": 28.17,
    "tip": 6.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 215,
    "tip_pct": 23.07
  },
  {
    "total_bill": 12.9,
    "tip": 1.1,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 216,
    "tip_pct": 8.53
  },
  {
    "total_bill": 28.15,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 5,
    "id": 217,
    "tip_pct": 10.66
  },
  {
    "total_bill": 11.59,
    "tip": 1.5,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 218,
    "tip_pct": 12.94
  },
  {
    "total_bill": 7.74,
    "tip": 1.44,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 219,
    "tip_pct": 18.6
  },
  {
    "total_bill": 30.14,
    "tip": 3.09,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 220,
    "tip_pct": 10.25
  },
  {
    "total_bill": 12.16,
    "tip": 2.2,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 2,
    "id": 221,
    "tip_pct": 18.09
  },
  {
    "total_bill": 13.42,
    "tip": 3.48,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 2,
    "id": 222,
    "tip_pct": 25.93
  },
  {
    "total_bill": 8.58,
    "tip": 1.92,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 1,
    "id": 223,
    "tip_pct": 22.38
  },
  {
    "total_bill": 15.98,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Fri",
    "time": "Lunch",
    "size": 3,
    "id": 224,
    "tip_pct": 18.77
  },
  {
    "total_bill": 13.42,
    "tip": 1.58,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 2,
    "id": 225,
    "tip_pct": 11.77
  },
  {
    "total_bill": 16.27,
    "tip": 2.5,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 2,
    "id": 226,
    "tip_pct": 15.37
  },
  {
    "total_bill": 10.09,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Fri",
    "time": "Lunch",
    "size": 2,
    "id": 227,
    "tip_pct": 19.82
  },
  {
    "total_bill": 20.45,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 228,
    "tip_pct": 14.67
  },
  {
    "total_bill": 13.28,
    "tip": 2.72,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 229,
    "tip_pct": 20.48
  },
  {
    "total_bill": 22.12,
    "tip": 2.88,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 230,
    "tip_pct": 13.02
  },
  {
    "total_bill": 24.01,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 4,
    "id": 231,
    "tip_pct": 8.33
  },
  {
    "total_bill": 15.69,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 232,
    "tip_pct": 19.12
  },
  {
    "total_bill": 11.61,
    "tip": 3.39,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 233,
    "tip_pct": 29.2
  },
  {
    "total_bill": 10.77,
    "tip": 1.47,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 234,
    "tip_pct": 13.65
  },
  {
    "total_bill": 15.53,
    "tip": 3.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 235,
    "tip_pct": 19.32
  },
  {
    "total_bill": 10.07,
    "tip": 1.25,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 236,
    "tip_pct": 12.41
  },
  {
    "total_bill": 12.6,
    "tip": 1.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 237,
    "tip_pct": 7.94
  },
  {
    "total_bill": 32.83,
    "tip": 1.17,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 238,
    "tip_pct": 3.56
  },
  {
    "total_bill": 35.83,
    "tip": 4.67,
    "sex": "Female",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 239,
    "tip_pct": 13.03
  },
  {
    "total_bill": 29.03,
    "tip": 5.92,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 3,
    "id": 240,
    "tip_pct": 20.39
  },
  {
    "total_bill": 27.18,
    "tip": 2.0,
    "sex": "Female",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 241,
    "tip_pct": 7.36
  },
  {
    "total_bill": 22.67,
    "tip": 2.0,
    "sex": "Male",
    "smoker": "Yes",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 242,
    "tip_pct": 8.82
  },
  {
    "total_bill": 17.82,
    "tip": 1.75,
    "sex": "Male",
    "smoker": "No",
    "day": "Sat",
    "time": "Dinner",
    "size": 2,
    "id": 243,
    "tip_pct": 9.82
  },
  {
    "total_bill": 18.78,
    "tip": 3.0,
    "sex": "Female",
    "smoker": "No",
    "day": "Thur",
    "time": "Dinner",
    "size": 2,
    "id": 244,
    "tip_pct": 15.97
  }
];

// Application State
const state = {
  rawData: [],
  filteredData: [],
  filters: {
    day: 'all',
    time: 'all',
    smoker: 'all',
    search: ''
  },
  sort: {
    col: 'id',
    asc: true
  },
  pagination: {
    page: 1,
    rowsPerPage: 10
  },
  viewMode: 'plotly', // 'plotly' or 'seaborn'
  histBins: 20
};

// Common Plotly Dark Navy Theme Options
const PLOTLY_LAYOUT_DEFAULTS = {
  paper_bgcolor: 'transparent',
  plot_bgcolor: 'rgba(15, 23, 42, 0.5)',
  font: {
    family: 'Inter, -apple-system, sans-serif',
    color: '#cbd5e1',
    size: 11
  },
  margin: { l: 55, r: 25, t: 35, b: 50 },
  hoverlabel: {
    bgcolor: '#0f172a',
    bordercolor: '#38bdf8',
    font: { family: 'Inter', color: '#f8fafc', size: 12 }
  },
  xaxis: {
    gridcolor: '#1e293b',
    zerolinecolor: '#334155',
    linecolor: '#334155',
    tickcolor: '#334155',
    tickfont: { color: '#94a3b8' }
  },
  yaxis: {
    gridcolor: '#1e293b',
    zerolinecolor: '#334155',
    linecolor: '#334155',
    tickcolor: '#334155',
    tickfont: { color: '#94a3b8' }
  }
};

const PLOTLY_CONFIG = {
  responsive: true,
  displayModeBar: false
};

// Initialize application on DOM content load
document.addEventListener('DOMContentLoaded', async () => {
  initNavigation();
  initEventListeners();
  await loadDataset();
  renderAll();
});

/**
 * Load dataset: attempts API first, then falls back to JSON or embedded records.
 */
async function loadDataset() {
  try {
    // Check if running on Flask backend
    const res = await fetch('/api/data');
    if (res.ok) {
      const json = await res.json();
      if (json && json.data && json.data.length > 0) {
        state.rawData = json.data.map((r, i) => ({
          id: i + 1,
          total_bill: Number(r.total_bill),
          tip: Number(r.tip),
          sex: r.sex,
          smoker: r.smoker,
          day: r.day,
          time: r.time,
          size: Number(r.size),
          tip_pct: Number((r.tip / r.total_bill * 100).toFixed(2))
        }));
        console.log(`[DataViz] Loaded ${state.rawData.length} records from Flask API`);
        state.filteredData = [...state.rawData];
        return;
      }
    }
  } catch (e) {
    // Not running via Flask API or network fetch failed
  }

  // Fallback to embedded data
  state.rawData = EMBEDDED_TIPS_DATA;
  state.filteredData = [...state.rawData];
  console.log(`[DataViz] Loaded ${state.rawData.length} records from authentic embedded dataset`);
}

/**
 * Filter data based on active controls
 */
function applyFilters() {
  state.filteredData = state.rawData.filter(row => {
    // Day filter
    if (state.filters.day !== 'all' && row.day.toLowerCase() !== state.filters.day.toLowerCase()) {
      return false;
    }
    // Time filter
    if (state.filters.time !== 'all' && row.time.toLowerCase() !== state.filters.time.toLowerCase()) {
      return false;
    }
    // Smoker filter
    if (state.filters.smoker !== 'all' && row.smoker.toLowerCase() !== state.filters.smoker.toLowerCase()) {
      return false;
    }
    // Search filter
    if (state.filters.search) {
      const q = state.filters.search.toLowerCase();
      const match = 
        row.total_bill.toString().includes(q) ||
        row.tip.toString().includes(q) ||
        row.day.toLowerCase().includes(q) ||
        row.time.toLowerCase().includes(q) ||
        row.sex.toLowerCase().includes(q) ||
        row.smoker.toLowerCase().includes(q) ||
        row.size.toString().includes(q);
      if (!match) return false;
    }
    return true;
  });

  // Reset pagination to first page
  state.pagination.page = 1;
}

/**
 * Re-render all dashboard components (KPI stats, charts, table)
 */
function renderAll() {
  applyFilters();
  renderKpiStats();
  renderCharts();
  renderTable();
  updateFilterBadges();
}

/**
 * Render KPI Top Stat Cards with dynamic math
 */
function renderKpiStats() {
  const data = state.filteredData;
  const total = data.length;

  document.getElementById('statTotalRecords').textContent = total;
  document.getElementById('sidebarRecordCount').textContent = `${total} Authentic Records`;
  document.getElementById('filteredRecordBadge').textContent = `${total} / ${state.rawData.length} records`;

  if (total === 0) {
    document.getElementById('statAvgBill').textContent = '$0.00';
    document.getElementById('statMedianBill').textContent = 'No records match filter';
    document.getElementById('statAvgTip').textContent = '$0.00';
    document.getElementById('statMedianTip').textContent = 'No records match filter';
    document.getElementById('statAvgTipPct').textContent = '0.00%';
    document.getElementById('statPeakDay').textContent = 'N/A';
    document.getElementById('statPeakDayTip').textContent = '$0.00';
    return;
  }

  const bills = data.map(d => d.total_bill).sort((a, b) => a - b);
  const tips = data.map(d => d.tip).sort((a, b) => a - b);
  const tipPcts = data.map(d => d.tip_pct);

  const avgBill = bills.reduce((a, b) => a + b, 0) / total;
  const avgTip = tips.reduce((a, b) => a + b, 0) / total;
  const avgTipPct = tipPcts.reduce((a, b) => a + b, 0) / total;

  const medianBill = calculateMedian(bills);
  const medianTip = calculateMedian(tips);
  const maxBill = Math.max(...bills);
  const maxTip = Math.max(...tips);

  // Peak day calculation
  const dayGroups = {};
  data.forEach(d => {
    if (!dayGroups[d.day]) dayGroups[d.day] = [];
    dayGroups[d.day].push(d.tip);
  });

  let peakDay = 'Sunday';
  let peakDayAvg = 0;
  for (const [day, dayTips] of Object.entries(dayGroups)) {
    const dayMean = dayTips.reduce((a, b) => a + b, 0) / dayTips.length;
    if (dayMean > peakDayAvg) {
      peakDayAvg = dayMean;
      peakDay = day;
    }
  }

  const dayNames = {
    'Thur': 'Thursday',
    'Fri': 'Friday',
    'Sat': 'Saturday',
    'Sun': 'Sunday'
  };

  document.getElementById('statAvgBill').textContent = `$${avgBill.toFixed(2)}`;
  document.getElementById('statMedianBill').textContent = `Median: $${medianBill.toFixed(2)} | Max: $${maxBill.toFixed(2)}`;

  document.getElementById('statAvgTip').textContent = `$${avgTip.toFixed(2)}`;
  document.getElementById('statMedianTip').textContent = `Median: $${medianTip.toFixed(2)} | Max: $${maxTip.toFixed(2)}`;

  document.getElementById('statAvgTipPct').textContent = `${avgTipPct.toFixed(2)}%`;
  document.getElementById('statPeakDay').textContent = dayNames[peakDay] || peakDay;
  document.getElementById('statPeakDayTip').textContent = `$${peakDayAvg.toFixed(2)} avg tip per table`;
}

/**
 * Render all 5 Charts
 */
function renderCharts() {
  if (state.viewMode === 'seaborn') {
    return; // Static images are visible
  }

  renderHistogram();
  renderBarChart();
  renderBoxPlot();
  renderScatterPlot();
  renderHeatmap();
}

/**
 * Chart 1: Distribution of Restaurant Bills (Histogram)
 */
function renderHistogram() {
  const container = document.getElementById('plotDistBills');
  if (!container || !window.Plotly) return;

  const bills = state.filteredData.map(d => d.total_bill);
  if (bills.length === 0) {
    Plotly.purge(container);
    return;
  }

  const avgBill = bills.reduce((a, b) => a + b, 0) / bills.length;
  const medianBill = calculateMedian([...bills].sort((a, b) => a - b));

  const traceHist = {
    x: bills,
    type: 'histogram',
    nbinsx: state.histBins,
    marker: {
      color: 'rgba(56, 189, 248, 0.75)',
      line: {
        color: '#0284c7',
        width: 1.2
      }
    },
    name: 'Total Bill Count',
    hovertemplate: 'Bill Range: $%{x}<br>Count: %{y} receipts<extra></extra>'
  };

  const layout = {
    ...PLOTLY_LAYOUT_DEFAULTS,
    title: false,
    xaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.xaxis,
      title: { text: 'Total Bill Amount ($)', font: { color: '#cbd5e1', size: 12 } },
      tickprefix: '$'
    },
    yaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.yaxis,
      title: { text: 'Frequency (Check Count)', font: { color: '#cbd5e1', size: 12 } }
    },
    shapes: [
      {
        type: 'line',
        x0: avgBill,
        x1: avgBill,
        y0: 0,
        y1: 1,
        yref: 'paper',
        line: { color: '#fbbf24', width: 2.2, dash: 'dash' }
      },
      {
        type: 'line',
        x0: medianBill,
        x1: medianBill,
        y0: 0,
        y1: 1,
        yref: 'paper',
        line: { color: '#22d3ee', width: 2, dash: 'dot' }
      }
    ],
    annotations: [
      {
        x: avgBill,
        y: 0.95,
        yref: 'paper',
        text: `Mean: $${avgBill.toFixed(2)}`,
        showarrow: true,
        arrowhead: 2,
        arrowcolor: '#fbbf24',
        arrowsize: 0.8,
        font: { color: '#fbbf24', size: 10, weight: 'bold' },
        bgcolor: 'rgba(15, 23, 42, 0.85)',
        bordercolor: '#fbbf24'
      },
      {
        x: medianBill,
        y: 0.80,
        yref: 'paper',
        text: `Median: $${medianBill.toFixed(2)}`,
        showarrow: true,
        arrowhead: 2,
        arrowcolor: '#22d3ee',
        arrowsize: 0.8,
        font: { color: '#22d3ee', size: 10, weight: 'bold' },
        bgcolor: 'rgba(15, 23, 42, 0.85)',
        bordercolor: '#22d3ee'
      }
    ]
  };

  Plotly.newPlot(container, [traceHist], layout, PLOTLY_CONFIG);
}

/**
 * Chart 2: Average Tip by Day (Bar Chart)
 */
function renderBarChart() {
  const container = document.getElementById('plotAvgTipDay');
  if (!container || !window.Plotly) return;

  const dayOrder = ['Thur', 'Fri', 'Sat', 'Sun'];
  const dayLabels = ['Thursday', 'Friday', 'Saturday', 'Sunday'];
  const dayColors = ['#38bdf8', '#818cf8', '#a855f7', '#ec4899'];

  const avgs = [];
  const counts = [];

  dayOrder.forEach(day => {
    const dayData = state.filteredData.filter(d => d.day === day);
    if (dayData.length > 0) {
      const mean = dayData.reduce((acc, d) => acc + d.tip, 0) / dayData.length;
      avgs.push(Number(mean.toFixed(2)));
      counts.push(dayData.length);
    } else {
      avgs.push(0);
      counts.push(0);
    }
  });

  const traceBars = {
    x: dayLabels,
    y: avgs,
    type: 'bar',
    marker: {
      color: dayColors,
      line: { color: '#0f172a', width: 1.5 }
    },
    text: avgs.map((v, i) => v > 0 ? `$${v.toFixed(2)} (n=${counts[i]})` : 'No Data'),
    textposition: 'outside',
    textfont: { color: '#f8fafc', size: 11, weight: 'bold' },
    hovertemplate: '<b>%{x}</b><br>Average Tip: $%{y:.2f}<extra></extra>'
  };

  const maxVal = Math.max(...avgs, 3.5);

  const layout = {
    ...PLOTLY_LAYOUT_DEFAULTS,
    yaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.yaxis,
      title: { text: 'Average Tip ($)', font: { color: '#cbd5e1', size: 12 } },
      range: [0, maxVal * 1.2],
      tickprefix: '$'
    },
    xaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.xaxis,
      title: { text: 'Day of the Week', font: { color: '#cbd5e1', size: 12 } }
    }
  };

  Plotly.newPlot(container, [traceBars], layout, PLOTLY_CONFIG);
}

/**
 * Chart 3: Distribution of Tips Across Days (Box Plot)
 */
function renderBoxPlot() {
  const container = document.getElementById('plotBoxTipDay');
  if (!container || !window.Plotly) return;

  const dayOrder = ['Thur', 'Fri', 'Sat', 'Sun'];
  const dayLabels = { 'Thur': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday' };
  const colors = { 'Thur': '#38bdf8', 'Fri': '#818cf8', 'Sat': '#a855f7', 'Sun': '#ec4899' };

  const traces = dayOrder.map(day => {
    const dayTips = state.filteredData.filter(d => d.day === day).map(d => d.tip);
    return {
      y: dayTips,
      type: 'box',
      name: dayLabels[day],
      boxpoints: 'outliers',
      jitter: 0.3,
      marker: {
        color: colors[day],
        outliercolor: '#fbbf24',
        size: 5
      },
      line: { width: 1.8 }
    };
  });

  const layout = {
    ...PLOTLY_LAYOUT_DEFAULTS,
    showlegend: false,
    yaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.yaxis,
      title: { text: 'Tip Amount ($)', font: { color: '#cbd5e1', size: 12 } },
      tickprefix: '$'
    },
    xaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.xaxis,
      title: { text: 'Day of Week', font: { color: '#cbd5e1', size: 12 } }
    }
  };

  Plotly.newPlot(container, traces, layout, PLOTLY_CONFIG);
}

/**
 * Chart 4: Relationship Between Total Bill and Tip (Scatter Plot)
 */
function renderScatterPlot() {
  const container = document.getElementById('plotScatterBillTip');
  if (!container || !window.Plotly) return;

  const data = state.filteredData;
  if (data.length === 0) {
    Plotly.purge(container);
    return;
  }

  const dinnerData = data.filter(d => d.time === 'Dinner');
  const lunchData = data.filter(d => d.time === 'Lunch');

  const traceDinner = {
    x: dinnerData.map(d => d.total_bill),
    y: dinnerData.map(d => d.tip),
    mode: 'markers',
    type: 'scatter',
    name: 'Dinner',
    marker: {
      color: '#38bdf8',
      size: 9,
      opacity: 0.85,
      line: { color: '#0369a1', width: 1 }
    },
    customdata: dinnerData.map(d => [d.day, d.size, d.tip_pct, d.smoker]),
    hovertemplate: 
      '<b>Dinner Service</b><br>' +
      'Total Bill: $%{x:.2f}<br>' +
      'Tip: $%{y:.2f} (%{customdata[2]}%)<br>' +
      'Day: %{customdata[0]} | Party: %{customdata[1]} guests<br>' +
      'Smoker: %{customdata[3]}<extra></extra>'
  };

  const traceLunch = {
    x: lunchData.map(d => d.total_bill),
    y: lunchData.map(d => d.tip),
    mode: 'markers',
    type: 'scatter',
    name: 'Lunch',
    marker: {
      color: '#fbbf24',
      size: 9,
      opacity: 0.85,
      line: { color: '#b45309', width: 1 }
    },
    customdata: lunchData.map(d => [d.day, d.size, d.tip_pct, d.smoker]),
    hovertemplate: 
      '<b>Lunch Service</b><br>' +
      'Total Bill: $%{x:.2f}<br>' +
      'Tip: $%{y:.2f} (%{customdata[2]}%)<br>' +
      'Day: %{customdata[0]} | Party: %{customdata[1]} guests<br>' +
      'Smoker: %{customdata[3]}<extra></extra>'
  };

  // Regression trendline
  const allX = data.map(d => d.total_bill);
  const allY = data.map(d => d.tip);
  const reg = calculateLinearRegression(allX, allY);

  const minX = Math.min(...allX);
  const maxX = Math.max(...allX);

  const traceTrend = {
    x: [minX, maxX],
    y: [reg.slope * minX + reg.intercept, reg.slope * maxX + reg.intercept],
    mode: 'lines',
    type: 'scatter',
    name: `Trend (r = ${reg.r.toFixed(3)})`,
    line: {
      color: '#cbd5e1',
      width: 2,
      dash: 'dash'
    },
    hoverinfo: 'skip'
  };

  const layout = {
    ...PLOTLY_LAYOUT_DEFAULTS,
    legend: {
      x: 0.02,
      y: 0.98,
      bgcolor: 'rgba(15, 23, 42, 0.85)',
      bordercolor: '#334155',
      borderwidth: 1,
      font: { color: '#f8fafc', size: 10 }
    },
    xaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.xaxis,
      title: { text: 'Total Bill ($)', font: { color: '#cbd5e1', size: 12 } },
      tickprefix: '$'
    },
    yaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.yaxis,
      title: { text: 'Tip ($)', font: { color: '#cbd5e1', size: 12 } },
      tickprefix: '$'
    }
  };

  Plotly.newPlot(container, [traceDinner, traceLunch, traceTrend], layout, PLOTLY_CONFIG);
}

/**
 * Chart 5: Correlation Heatmap
 */
function renderHeatmap() {
  const container = document.getElementById('plotHeatmap');
  if (!container || !window.Plotly) return;

  const data = state.filteredData;
  if (data.length < 2) {
    Plotly.purge(container);
    return;
  }

  const bills = data.map(d => d.total_bill);
  const tips = data.map(d => d.tip);
  const sizes = data.map(d => d.size);

  const rBillTip = calculateCorrelation(bills, tips);
  const rBillSize = calculateCorrelation(bills, sizes);
  const rTipSize = calculateCorrelation(tips, sizes);

  const labels = ['Total Bill', 'Tip', 'Party Size'];
  const zValues = [
    [1.000, rBillTip, rBillSize],
    [rBillTip, 1.000, rTipSize],
    [rBillSize, rTipSize, 1.000]
  ];

  const textAnnotations = zValues.map(row => row.map(v => v.toFixed(3)));

  const traceHeatmap = {
    z: zValues,
    x: labels,
    y: labels,
    type: 'heatmap',
    colorscale: [
      [0.0, '#0f172a'],
      [0.3, '#1e3a8a'],
      [0.6, '#0284c7'],
      [1.0, '#38bdf8']
    ],
    zmin: 0.0,
    zmax: 1.0,
    showscale: true,
    colorbar: {
      title: 'Pearson (r)',
      titleside: 'top',
      tickcolor: '#334155',
      tickfont: { color: '#94a3b8', size: 10 },
      len: 0.9,
      thickness: 14
    },
    hovertemplate: 'Variables: %{x} & %{y}<br>Correlation: <b>%{z:.3f}</b><extra></extra>'
  };

  // Text annotations on heatmap cells
  const annotations = [];
  for (let i = 0; i < labels.length; i++) {
    for (let j = 0; j < labels.length; j++) {
      annotations.push({
        x: labels[j],
        y: labels[i],
        text: `<b>${textAnnotations[i][j]}</b>`,
        font: {
          color: zValues[i][j] > 0.6 ? '#ffffff' : '#cbd5e1',
          size: 14
        },
        showarrow: false
      });
    }
  }

  const layout = {
    ...PLOTLY_LAYOUT_DEFAULTS,
    annotations: annotations,
    xaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.xaxis,
      tickfont: { color: '#f8fafc', size: 12, weight: 'bold' }
    },
    yaxis: {
      ...PLOTLY_LAYOUT_DEFAULTS.yaxis,
      tickfont: { color: '#f8fafc', size: 12, weight: 'bold' }
    }
  };

  Plotly.newPlot(container, [traceHeatmap], layout, PLOTLY_CONFIG);
}

/**
 * Render Data Explorer Table
 */
function renderTable() {
  const tbody = document.getElementById('tableBody');
  if (!tbody) return;

  // Sorting
  const sorted = [...state.filteredData].sort((a, b) => {
    let vA = a[state.sort.col];
    let vB = b[state.sort.col];

    if (typeof vA === 'string') {
      return state.sort.asc ? vA.localeCompare(vB) : vB.localeCompare(vA);
    }
    return state.sort.asc ? vA - vB : vB - vA;
  });

  // Pagination slice
  const total = sorted.length;
  const rpp = state.pagination.rowsPerPage;
  const page = state.pagination.page;
  const startIdx = (page - 1) * rpp;
  const pageData = sorted.slice(startIdx, startIdx + rpp);

  if (pageData.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="9" style="text-align: center; padding: 40px; color: var(--text-muted);">
          <i class="fa-solid fa-folder-open" style="font-size: 2rem; margin-bottom: 12px; display: block; opacity: 0.5;"></i>
          No dining records match your search and filter criteria.
        </td>
      </tr>
    `;
  } else {
    tbody.innerHTML = pageData.map(row => `
      <tr>
        <td style="color: var(--text-dim); font-size: 0.8rem;">#${row.id}</td>
        <td style="font-weight: 700; color: #ffffff;">$${row.total_bill.toFixed(2)}</td>
        <td style="font-weight: 700; color: var(--accent-cyan);">$${row.tip.toFixed(2)}</td>
        <td style="color: var(--text-secondary);">${row.tip_pct.toFixed(1)}%</td>
        <td><span class="badge-pill" style="font-size: 0.75rem;">${row.day}</span></td>
        <td>
          <span class="tag-badge ${row.time === 'Dinner' ? 'tag-dinner' : 'tag-lunch'}">
            ${row.time}
          </span>
        </td>
        <td style="color: var(--text-secondary);">${row.sex}</td>
        <td>
          <span class="tag-badge ${row.smoker === 'Yes' ? 'tag-smoker-yes' : 'tag-smoker-no'}">
            ${row.smoker === 'Yes' ? 'Smoker' : 'Non-Smoker'}
          </span>
        </td>
        <td style="font-weight: 600;">
          <i class="fa-solid fa-users" style="color: var(--text-dim); font-size: 0.8rem; margin-right: 4px;"></i>
          ${row.size}
        </td>
      </tr>
    `).join('');
  }

  // Update record summary
  const summaryEl = document.getElementById('tableRecordSummary');
  if (total === 0) {
    summaryEl.textContent = 'Showing 0 records';
  } else {
    const endIdx = Math.min(startIdx + rpp, total);
    summaryEl.textContent = `Showing ${startIdx + 1} to ${endIdx} of ${total} records (Filtered from ${state.rawData.length})`;
  }

  renderPaginationControls(total);
}

/**
 * Render pagination buttons
 */
function renderPaginationControls(totalRecords) {
  const container = document.getElementById('paginationControls');
  if (!container) return;

  const totalPages = Math.ceil(totalRecords / state.pagination.rowsPerPage) || 1;
  const current = state.pagination.page;

  let html = `
    <button class="page-btn" id="prevPageBtn" ${current <= 1 ? 'disabled' : ''}>
      <i class="fa-solid fa-chevron-left"></i>
    </button>
  `;

  // Determine page numbers range to display
  let startPage = Math.max(1, current - 2);
  let endPage = Math.min(totalPages, current + 2);

  if (startPage > 1) {
    html += `<button class="page-btn" data-page="1">1</button>`;
    if (startPage > 2) html += `<span style="color: var(--text-dim); padding: 0 4px;">...</span>`;
  }

  for (let p = startPage; p <= endPage; p++) {
    html += `<button class="page-btn ${p === current ? 'active' : ''}" data-page="${p}">${p}</button>`;
  }

  if (endPage < totalPages) {
    if (endPage < totalPages - 1) html += `<span style="color: var(--text-dim); padding: 0 4px;">...</span>`;
    html += `<button class="page-btn" data-page="${totalPages}">${totalPages}</button>`;
  }

  html += `
    <button class="page-btn" id="nextPageBtn" ${current >= totalPages ? 'disabled' : ''}>
      <i class="fa-solid fa-chevron-right"></i>
    </button>
  `;

  container.innerHTML = html;

  // Add click handlers for pages
  container.querySelectorAll('.page-btn[data-page]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      state.pagination.page = parseInt(e.currentTarget.getAttribute('data-page'));
      renderTable();
    });
  });

  const prevBtn = document.getElementById('prevPageBtn');
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (state.pagination.page > 1) {
        state.pagination.page--;
        renderTable();
      }
    });
  }

  const nextBtn = document.getElementById('nextPageBtn');
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (state.pagination.page < totalPages) {
        state.pagination.page++;
        renderTable();
      }
    });
  }
}

/**
 * Update filter controls to reflect state
 */
function updateFilterBadges() {
  const daySel = document.getElementById('filterDay');
  const timeSel = document.getElementById('filterTime');
  const smokerSel = document.getElementById('filterSmoker');
  const tableDaySel = document.getElementById('tableDayFilter');
  const tableTimeSel = document.getElementById('tableTimeFilter');
  const tableSmokerSel = document.getElementById('tableSmokerFilter');

  if (daySel) daySel.value = state.filters.day;
  if (timeSel) timeSel.value = state.filters.time;
  if (smokerSel) smokerSel.value = state.filters.smoker;

  if (tableDaySel) tableDaySel.value = state.filters.day;
  if (tableTimeSel) tableTimeSel.value = state.filters.time;
  if (tableSmokerSel) tableSmokerSel.value = state.filters.smoker;
}

/**
 * Initialize DOM Event Listeners
 */
function initEventListeners() {
  // Dashboard ribbon filters
  const filterDay = document.getElementById('filterDay');
  const filterTime = document.getElementById('filterTime');
  const filterSmoker = document.getElementById('filterSmoker');
  const filterResetBtn = document.getElementById('filterResetBtn');
  const globalResetBtn = document.getElementById('globalResetBtn');
  const tableResetBtn = document.getElementById('tableResetBtn');

  const onFilterChange = () => {
    state.filters.day = filterDay.value;
    state.filters.time = filterTime.value;
    state.filters.smoker = filterSmoker.value;
    renderAll();
  };

  if (filterDay) filterDay.addEventListener('change', onFilterChange);
  if (filterTime) filterTime.addEventListener('change', onFilterChange);
  if (filterSmoker) filterSmoker.addEventListener('change', onFilterChange);

  // Table filters synchronization
  const tableDay = document.getElementById('tableDayFilter');
  const tableTime = document.getElementById('tableTimeFilter');
  const tableSmoker = document.getElementById('tableSmokerFilter');

  if (tableDay) {
    tableDay.addEventListener('change', () => {
      state.filters.day = tableDay.value;
      renderAll();
    });
  }
  if (tableTime) {
    tableTime.addEventListener('change', () => {
      state.filters.time = tableTime.value;
      renderAll();
    });
  }
  if (tableSmoker) {
    tableSmoker.addEventListener('change', () => {
      state.filters.smoker = tableSmoker.value;
      renderAll();
    });
  }

  // Reset filters
  const resetAllFilters = () => {
    state.filters.day = 'all';
    state.filters.time = 'all';
    state.filters.smoker = 'all';
    state.filters.search = '';
    const searchInput = document.getElementById('tableSearchInput');
    if (searchInput) searchInput.value = '';
    renderAll();
  };

  if (filterResetBtn) filterResetBtn.addEventListener('click', resetAllFilters);
  if (globalResetBtn) globalResetBtn.addEventListener('click', resetAllFilters);
  if (tableResetBtn) tableResetBtn.addEventListener('click', resetAllFilters);

  // Search input with debounce
  const searchInput = document.getElementById('tableSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.filters.search = e.target.value.trim();
      applyFilters();
      renderTable();
      renderKpiStats();
      renderCharts();
    });
  }

  // Rows per page
  const rowsPerPageSel = document.getElementById('rowsPerPage');
  if (rowsPerPageSel) {
    rowsPerPageSel.addEventListener('change', (e) => {
      state.pagination.rowsPerPage = parseInt(e.target.value);
      state.pagination.page = 1;
      renderTable();
    });
  }

  // Table header sorting
  const tableHeaders = document.querySelectorAll('#dataTable th[data-col]');
  tableHeaders.forEach(th => {
    th.addEventListener('click', () => {
      const col = th.getAttribute('data-col');
      if (state.sort.col === col) {
        state.sort.asc = !state.sort.asc;
      } else {
        state.sort.col = col;
        state.sort.asc = true;
      }
      // Update icons
      tableHeaders.forEach(h => {
        const icon = h.querySelector('i');
        if (icon) icon.className = 'fa-solid fa-sort';
      });
      const currentIcon = th.querySelector('i');
      if (currentIcon) {
        currentIcon.className = state.sort.asc ? 'fa-solid fa-sort-up' : 'fa-solid fa-sort-down';
        currentIcon.style.color = 'var(--primary-blue)';
      }
      renderTable();
    });
  });

  // View Mode: Plotly vs Seaborn
  const btnPlotly = document.getElementById('btnModePlotly');
  const btnSeaborn = document.getElementById('btnModeSeaborn');

  const setViewMode = (mode) => {
    state.viewMode = mode;
    if (mode === 'plotly') {
      btnPlotly.classList.add('active');
      btnSeaborn.classList.remove('active');
      document.querySelectorAll('.chart-container-plot').forEach(el => el.style.display = 'block');
      document.querySelectorAll('.static-image-container').forEach(el => el.style.display = 'none');
      renderCharts();
    } else {
      btnSeaborn.classList.add('active');
      btnPlotly.classList.remove('active');
      document.querySelectorAll('.chart-container-plot').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.static-image-container').forEach(el => el.style.display = 'block');
    }
  };

  if (btnPlotly) btnPlotly.addEventListener('click', () => setViewMode('plotly'));
  if (btnSeaborn) btnSeaborn.addEventListener('click', () => setViewMode('seaborn'));

  // Histogram bin selector
  const histBinSelect = document.getElementById('histBinSelect');
  if (histBinSelect) {
    histBinSelect.addEventListener('change', (e) => {
      state.histBins = parseInt(e.target.value);
      renderHistogram();
    });
  }

  // Export CSV
  const exportBtn = document.getElementById('exportCsvBtn');
  if (exportBtn) {
    exportBtn.addEventListener('click', exportFilteredDataToCsv);
  }
}

/**
 * Initialize Navigation & Smooth Scroll
 */
function initNavigation() {
  const mobileToggle = document.getElementById('mobileToggle');
  const sidebar = document.getElementById('sidebar');

  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (window.innerWidth <= 860 && 
          !sidebar.contains(e.target) && 
          !mobileToggle.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  // Smooth scroll and active link update
  const navLinks = document.querySelectorAll('.sidebar-nav a[data-nav]');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPos = window.scrollY + 120;

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      if (link.getAttribute('data-nav') === current) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  });
}

/**
 * Export filtered records to CSV
 */
function exportFilteredDataToCsv() {
  const data = state.filteredData;
  if (!data || data.length === 0) {
    alert('No records available to export.');
    return;
  }

  const headers = ['id', 'total_bill', 'tip', 'tip_pct', 'day', 'time', 'sex', 'smoker', 'size'];
  const csvRows = [];
  csvRows.push(headers.join(','));

  data.forEach(row => {
    const values = headers.map(h => row[h]);
    csvRows.push(values.join(','));
  });

  const csvString = csvRows.join('\n');
  const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.setAttribute('href', url);
  link.setAttribute('download', `seaborn_tips_export_${state.filters.day}_${state.filters.time}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

/**
 * Math Helper: Calculate Median
 */
function calculateMedian(sortedArray) {
  if (!sortedArray || sortedArray.length === 0) return 0;
  const mid = Math.floor(sortedArray.length / 2);
  return sortedArray.length % 2 !== 0
    ? sortedArray[mid]
    : (sortedArray[mid - 1] + sortedArray[mid]) / 2;
}

/**
 * Math Helper: Pearson Correlation Coefficient (r)
 */
function calculateCorrelation(x, y) {
  const n = x.length;
  if (n < 2) return 0;

  const meanX = x.reduce((a, b) => a + b, 0) / n;
  const meanY = y.reduce((a, b) => a + b, 0) / n;

  let num = 0;
  let denX = 0;
  let denY = 0;

  for (let i = 0; i < n; i++) {
    const dx = x[i] - meanX;
    const dy = y[i] - meanY;
    num += dx * dy;
    denX += dx * dx;
    denY += dy * dy;
  }

  const den = Math.sqrt(denX * denY);
  return den === 0 ? 0 : Number((num / den).toFixed(4));
}

/**
 * Math Helper: Simple Linear Regression (y = mx + c)
 */
function calculateLinearRegression(x, y) {
  const n = x.length;
  if (n < 2) return { slope: 0, intercept: 0, r: 0 };

  const meanX = x.reduce((a, b) => a + b, 0) / n;
  const meanY = y.reduce((a, b) => a + b, 0) / n;

  let num = 0;
  let den = 0;

  for (let i = 0; i < n; i++) {
    const dx = x[i] - meanX;
    num += dx * (y[i] - meanY);
    den += dx * dx;
  }

  const slope = den === 0 ? 0 : num / den;
  const intercept = meanY - slope * meanX;
  const r = calculateCorrelation(x, y);

  return { slope, intercept, r };
}
