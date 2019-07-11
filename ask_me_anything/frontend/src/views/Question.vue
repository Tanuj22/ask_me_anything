<template>
  <div class="single-question mt-2">
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      
      <p class="mb-0">Posted by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr>
      
    <div v-if="question" class="container">
      <AnswerComponent 
        v-for="answer in answers"
        :answer="answer"
        :requestUser="requestUser"
        :key="answer.id"
        @delete-answer="deleteAnswer"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    AnswerComponent,
    
  },
  data() {
    return {
      question: {},
      answers: [],
      next: null,
      loadingAnswers: false,
      newAnswerBody: null,
      
    }
  },
  computed: {
    isQuestionAuthor() {
      return this.question.author === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    
    getQuestionData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.question = data;
            this.userHasAnswered = data.user_has_answered;
            this.setPageTitle(data.content)
          } else {
            this.question = null;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    },
    getQuestionAnswers() {
      // get a page of answers for a single question from the REST API's paginated 'Questions Endpoint'
      let endpoint = `/api/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint)
        .then(data => {
          this.answers.push(...data.results);
          this.loadingAnswers = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
    
    
  },
  created() {
    this.getQuestionData()
    this.getQuestionAnswers()
    
  }
}
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #DC3545;
}

.answer-added {
  font-weight: bold;
  color: green;
}

.error {
  font-weight: bold;
  color: red; 
}
</style>
