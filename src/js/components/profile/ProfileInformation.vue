<template>
	<div class="card">
		<div class="card-body">
			<h1>My Profile</h1>
			<hr />

			<div class="row">
				<div class="col-md-4">
					<strong>User Details</strong>
					<p class="text-instructions">Please update your details.</p>
				</div>
				<div class="col-md-8">
					<p>
						<strong>Username: </strong>{{ userResults[0].username }}
					</p>
					<div class="row">
						<div class="col-md-6">
							<label>
								First Name:
								<validation-rendering
									v-bind:error-list="v$.firstNameModel.$errors"
								></validation-rendering>
								<br />
							</label>
							<input
								type="text"
								v-model="firstNameModel"
								class="form-control"
							/>
						</div>
						<div class="col-md-6">
							<label>
								Last Name:
								<validation-rendering
									v-bind:error-list="v$.firstNameModel.$errors"
								></validation-rendering>
								<br />
							</label>
							<input
								type="text"
								v-model="lastNameModel"
								class="form-control"
							/>
						</div>
					</div>

					<div class="spacer"></div>

					<div class="row">
						<div class="col-md-6">
							<label> Email: </label>
							<input
								type="email"
								v-model="emailModel"
								class="form-control"
								disabled="true"
							/>
						</div>
					</div>
				</div>
			</div>
			<hr />

			<!-- UPDATE USER -->
			<div class="row submit-row">
				<div class="col-md-12">
					<a
						href="javascript:void(0)"
						class="btn btn-primary save-changes"
						v-on:click="updateUser"
					>
						Update User Details
					</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	const axios = require("axios");

	//Validations
	import useVuelidate from "@vuelidate/core";
	import { required, maxLength } from "@vuelidate/validators";
	import ValidationRendering from "../validation/ValidationRendering.vue";

	//Mixins
	import errorModalMixin from "../../mixins/errorModalMixin";
	import loadingModalMixin from "../../mixins/loadingModalMixin";

	export default {
		name: "ProfileInformation",
		setup() {
			return { v$: useVuelidate() };
		},
		props: {
			rootUrl: {
				type: String,
				default: "/",
			},
			staticUrl: {
				type: String,
				default: "/",
			},
			userResults: {
				type: Array,
				default: () => {
					return [];
				},
			},
		},
		components: {
			ValidationRendering,
		},
		data() {
			return {
				emailModel: this.userResults[0].email,
				firstNameModel: this.userResults[0].first_name,
				lastNameModel: this.userResults[0].last_name,
			};
		},
		mixins: [errorModalMixin, loadingModalMixin],
		validations() {
			return {
				lastNameModel: {
					required,
					maxLength: maxLength(255),
				},
				firstNameModel: {
					required,
					maxLength: maxLength(255),
				},
			};
		},
		methods: {
			updateUser() {
				//Check form validation
				this.v$.$touch();

				if (this.v$.$invalid) {
					this.showValidationErrorModal();

					//Just return - as we do not need to do the rest of this function
					return;
				}

				//Create data_to_send
				const data_to_send = new FormData();
				data_to_send.set("username", this.userResults[0].id);
				data_to_send.set("first_name", this.firstNameModel);
				data_to_send.set("last_name", this.lastNameModel);

				//Open up the loading modal
				this.showLoadingModal("Project");

				//Send data via axios
				axios
					.post(
						`${this.rootUrl}profile_information/update_data/`,
						data_to_send
					)
					.then((response) => {
						//Notify user of success update
						this.closeLoadingModal();
					})
					.catch((error) => {
						//There was an error
						this.showErrorModal(error, "profile");
					});
			},
		},
		mounted() {
			//Send Root URL to VueX
			this.$store.commit({
				type: "updateUrl",
				rootUrl: this.rootUrl,
				staticUrl: this.staticUrl,
			});
		},
	};
</script>

<style></style>