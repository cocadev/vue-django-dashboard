<template>
  <div class="settings-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-12">
          <h1 class="text-xs-center">{{ message }}</h1>
          <span v-once>This will never change: {{ message }}</span>

          <span v-bind:title="bindmessage">
            Hover your mouse over me for a few seconds to see my dynamically
            bound title!
          </span>
          <hr />
          <span v-if="react">I am a React Expert.</span>
          <span v-if="!react">I am a Vue Expert.</span>
          <hr />

          <ol>
            <li v-for="todo in todos" v-bind:key="todo">
              {{ todo.text }}
            </li>
          </ol>

          <hr />
          <button v-on:click="reverseMessage">Reverse Message</button>

          <hr />
          <input v-model="message" />

          <hr />
          <ol>
            <li v-for="grocery in groceryList" v-bind:key="grocery">
              {{ grocery.text }}
            </li>
          </ol>
          <hr />

          <button v-bind:disabled="isButtonDisabled">Button</button>

          <hr />

          <div>{{ fullName }}</div>
          <div>{{ GivenName }}</div>

          <hr />

          <div>
            <p>
              Ask a yes/no question:
              <input v-model="question" />
            </p>
            <p>{{ answer }}</p>
          </div>

          <hr />

          <div
            class="static"
            v-bind:class="{ active: isActive, 'text-danger': hasError }"
          >
            Hello Panda
          </div>
          <div v-bind:class="classObject">Do not worry about Panda.</div>
          <div v-bind:class="[activeClass, errorClass]">Panda Warrior</div>
          <div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>

          <hr />
          <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">
            Hello Brother
          </div>
          <div v-bind:style="styleObject">Greet Purple</div>

          <hr />

          <h1 v-if="awesome">Vue is awesome!</h1>
          <h1 v-else>Oh no 😢</h1>
          <template v-if="ok">
            <h1>Title</h1>
            <p>Paragraph 1</p>
            <p>Paragraph 2</p>
          </template>
          <div v-if="Math.random() > 0.5">
            Now you see me
          </div>
          <div v-else>
            Now you don't
          </div>
          <div v-if="type === 'A'">
            A
          </div>
          <div v-else-if="type === 'B'">
            B
          </div>
          <div v-else-if="type === 'C'">
            C
          </div>
          <div v-else>
            Not A/B/C
          </div>
          <hr />

          <template v-if="loginType === 'username'">
            <label>Username</label>
            <input placeholder="Enter your username" key="username-input" />
          </template>
          <template v-else>
            <label>Email</label>
            <input placeholder="Enter your email address" key="email-input" />
          </template>
          <h1 v-show="ok">Hello!</h1>

          <hr />

          <ul id="example-2">
            <li v-for="item in items" v-bind:key="item">
              {{ item.message }}
            </li>
            <li v-for="(item, index) in items" v-bind:key="(item, index)">
              {{ parentMessage }} - {{ index }} - {{ item.message }}
            </li>
          </ul>

          <ul id="v-for-object" class="demo">
            <li v-for="value in object" v-bind:key="value">
              {{ value }}
            </li>
          </ul>

          <div v-for="(value, name) in object" v-bind:key="(value, name)">
            {{ name }}: {{ value }}
          </div>

          <div
            v-for="(value, name, index) in object"
            v-bind:key="(value, name, index)"
          >
            {{ index }}. {{ name }}: {{ value }}
          </div>

          <hr />

          <li v-for="n in evenNumbers" v-bind:key="n">{{ n }}</li>
          <li v-for="n in even(numbers)" v-bind:key="n">{{ n }}</li>

          <span v-for="n in 10" v-bind:key="n">{{ n }} </span>

          <ul>
            <template v-for="item in items">
              <li v-bind:key="item">{{ item.msg }}</li>
              <li v-bind:key="item" class="divider" role="presentation"></li>
            </template>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  name: "RwvTest",
  data: function() {
    return {
      message: "Hello Vue!",
      bindmessage: "You loaded this page on " + new Date().toLocaleString(),
      react: false,
      todos: [
        { text: "Learn JavaScript" },
        { text: "Learn Vue" },
        { text: "Build something awesome" }
      ],
      groceryList: [
        { id: 0, text: "Vegetables" },
        { id: 1, text: "Cheese" },
        { id: 2, text: "Whatever else humans are supposed to eat" }
      ],
      isButtonDisabled: true,
      firstName: "Eugene",
      lastName: "Pizzerbert",
      // fullName: 'Panda DEV'

      question: "",
      answer: "I cannot give you an answer until you ask a question!",

      isActive: true,
      hasError: true,
      // classObject: {
      //   active: true,
      //   'text-success': true
      // },
      activeClass: "active",
      errorClass: "text-danger",

      activeColor: "blue",
      fontSize: 30,

      styleObject: {
        color: "purple",
        fontSize: "43px"
      },
      items: [{ message: "Foo" }, { message: "Bar" }],
      parentMessage: "Parent",
      object: {
        title: "How to do lists in Vue",
        author: "Jane Doe",
        publishedAt: "2016-04-10"
      },
      numbers: [1, 2, 3, 4, 5]
    };
  },
  computed: {
    fullName: function() {
      return this.firstName + " " + this.lastName;
    },
    GivenName: {
      get: function() {
        return this.firstName + " " + this.lastName;
      },
      set: function(newValue) {
        var names = newValue.split(" ");
        this.firstName = names[0];
        this.lastName = names[names.length - 1];
      }
    },
    classObject: function() {
      return {
        active: this.isActive && !this.error,
        "text-danger": this.error && this.error.type === "fatal"
      };
    },
    evenNumbers: function() {
      return this.numbers.filter(function(number) {
        return number % 2 === 0;
      });
    }
  },
  watch: {
    firstName: function(val) {
      this.fullName = val + " " + this.lastName;
    },
    lastName: function(val) {
      this.fullName = this.firstName + " " + val;
    },

    // whenever question changes, this function will run
    question: function() {
      this.answer = "Waiting for you to stop typing...";
      this.debouncedGetAnswer();
    }
  },
  created: function() {
    // _.debounce is a function provided by lodash to limit how
    // often a particularly expensive operation can be run.
    // In this case, we want to limit how often we access
    // yesno.wtf/api, waiting until the user has completely
    // finished typing before making the ajax request. To learn
    // more about the _.debounce function (and its cousin
    // _.throttle), visit: https://lodash.com/docs#debounce
    this.debouncedGetAnswer = _.debounce(this.getAnswer, 500);
  },
  methods: {
    reverseMessage: function() {
      console.log("Hello Eugene: " + new Date());
      this.message = this.message
        .split("")
        .reverse()
        .join("");
    },
    getAnswer: function() {
      if (this.question.indexOf("?") === -1) {
        this.answer = "Questions usually contain a question mark. ;-)";
        return;
      }
      this.answer = "Thinking...";
      var vm = this;
      axios
        .get("https://yesno.wtf/api")
        .then(function(response) {
          vm.answer = _.capitalize(response.data.answer);
        })
        .catch(function(error) {
          vm.answer = "Error! Could not reach the API. " + error;
        });
    },
    even: function(numbers) {
      return numbers.filter(function(number) {
        return number % 2 === 1;
      });
    }
  }
};
</script>
