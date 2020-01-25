<template>
  <div id="contacts">
    <ul>
      Useres antigos.
      <li v-for="post in posts" v-bind:key="post" v-text="post.user_obj.username"></li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: null
    };
  },
  /* eslint-disable no-console */
  mounted: function() {
    // this.$http
    //   .post(
    //     "http://spotnow.westeurope.cloudapp.azure.com:8000/api/owner-add/",
    //     {
    //       // "user": {
    //       //   "username": "owner3",
    //       //   "password": "owner3spotnow",
    //       //   "email": "owner3@gmail.com"
    //       // },
    //       // "nif": "1234",
    //       // "telephone": "1234"
    //     }
    //   )
    //   .then(response => console.log(response));

    this.$http
      .get("http://spotnow.westeurope.cloudapp.azure.com:8000/api/owners/")
      .then(response => (this.posts = response.data))
      .finally(() => console.log("ola"));
  }
  /* eslint-enable no-console */
};
</script>

<style scoped>
.section-heading {
  font-size: 40px;
  margin-top: 0;
  margin-bottom: 15px;
}

h3.section-subheading {
  font-size: 16px;
  font-weight: 400;
  font-style: italic;
  margin-bottom: 75px;
  text-transform: none;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.topic-heading {
  margin: 15px 0;
}
</style>