<template>
  <div class="home">
    <h1>MedPredict-Health Diagnosis</h1>

    <!-- Symptom Input Section -->
    <section class="symptom-input">
      <h2>Enter your symptoms</h2>
      <textarea v-model="symptoms" placeholder="Describe your symptoms here..."></textarea>
      <button @click="submitSymptoms">Submit Symptoms</button>
    </section>

    <!-- Predictions Section -->
    <section v-if="predictions.length" class="predictions">
      <h2>Disease Predictions</h2>
      <ul>
        <li v-for="(prediction, index) in predictions" :key="index">
          <span>{{ prediction.name }} - Likelihood: {{ prediction.likelihood }}%</span>
          <button @click="explorePrediction(prediction.name)">Explore Further</button>
        </li>
      </ul>
    </section>

    <!-- Questionnaire Section -->
    <section v-if="showQuestions" class="questionnaire">
      <h2>Follow-Up Questions</h2>
      <div v-for="(question, index) in questionnaire" :key="index">
        <p>{{ question.question }}</p>
        <select v-model="answers[index]">
          <option v-for="option in question.options" :key="option">{{ option }}</option>
        </select>
      </div>
      <button @click="submitAnswers">Submit Answers</button>
    </section>

    <!-- Recommendations Section -->
    <section v-if="recommendations.length">
      <h2>Recommendations</h2>
      <ul>
        <li v-for="recommendation in recommendations" :key="recommendation">
          {{ recommendation }}
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      symptoms: '',
      predictions: [],
      showQuestions: false,
      questionnaire: [
        { question: 'How severe is your cough?', options: ['Mild', 'Moderate', 'Severe'] },
        { question: 'Have you experienced a fever in the last 48 hours?', options: ['Yes', 'No'] },
        { question: 'How would you rate your fatigue level?', options: ['Low', 'Moderate', 'High'] },
        { question: 'Are you experiencing any difficulty breathing?', options: ['Yes', 'Sometimes', 'Not at all'] }
      ],
      answers: [],
      recommendations: []
    };
  },
  methods: {
    async submitSymptoms() {
      try {
        const symptomsDict = {
          Fever: this.symptoms.includes('Fever') ? 'Yes' : 'No',
          Cough: this.symptoms.includes('Cough') ? 'Yes' : 'No',
          Fatigue: this.symptoms.includes('Fatigue') ? 'Yes' : 'No',
          'Difficulty Breathing': this.symptoms.includes('Difficulty Breathing') ? 'Yes' : 'No'
        };

        const response = await axios.post('http://127.0.0.1:5000/predict', {
          symptoms: symptomsDict
        });
        this.predictions = [{ name: response.data.disease, likelihood: 100 }];
        this.showQuestions = true;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async submitAnswers() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/submit_answers', {
          answers: this.answers
        });
        this.recommendations = response.data;
        this.showQuestions = false;
      } catch (error) {
        console.error('Error:', error);
      }
    },
    explorePrediction(diseaseName) {
      const googleSearchUrl = `https://www.google.com/search?q=${encodeURIComponent(diseaseName)}`;
      window.open(googleSearchUrl, '_blank');
    }
  }
};
</script>