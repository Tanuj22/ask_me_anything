<template>
  <div class="single-question mt-2">
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      
      <p class="mb-0">Posted by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr>
      
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    
  },
  data() {
    return {
      question: {},
      
    }
  },
  
  methods: {
    setPageTitle(title) {
      // set a given title string as the webpage title
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
    
     
    
    },
    
  
  created() {
    this.getQuestionData()
    
  }
}
</script>

<style scoped>

</style>
