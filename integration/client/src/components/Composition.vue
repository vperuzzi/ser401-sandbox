<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Piano Music</h1>
        <hr />
        <br /><br />
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.composition-modal
        >
          Add Composition
        </button>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Composer</th>
              <th scope="col">Finished?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(composition, index) in compositions" :key="index">
              <td>{{ composition.title }}</td>
              <td>{{ composition.composer }}</td>
              <td>
                <span v-if="composition.finished">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      ref="addCompositionModal"
      id="composition-modal"
      title="Add a new composition"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-title-group"
          label="Title:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addCompositionForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-composer-group"
          label="Composer:"
          label-for="form-composer-input"
        >
          <b-form-input
            id="form-composer-input"
            type="text"
            v-model="addCompositionForm.composer"
            required
            placeholder="Enter composer"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-finished-group">
          <b-form-checkbox-group
            v-model="addCompositionForm.finished"
            id="form-checks"
          >
            <b-form-checkbox value="true">Finished?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      compositions: [],
      addCompositionForm: {
        title: '',
        composer: '',
        finished: [],
      },
    };
  },
  methods: {
    getCompositions() {
      const path = 'http://localhost:5000/compositions';
      axios
        .get(path)
        .then((res) => {
          this.compositions = res.data.compositions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addComposition(payload) {
      const path = 'http://localhost:5000/compositions';
      axios
        .post(path, payload)
        .then(() => {
          this.getCompositions();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCompositions();
        });
    },
    initForm() {
      this.addCompositionForm.title = '';
      this.addCompositionForm.composer = '';
      this.addCompositionForm.finished = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCompositionModal.hide();
      let finished = false;
      if (this.addCompositionForm.finished[0]) finished = true;
      const payload = {
        title: this.addCompositionForm.title,
        composer: this.addCompositionForm.composer,
        finished,
      };
      this.addComposition(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCompositionModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getCompositions();
  },
};
</script>
