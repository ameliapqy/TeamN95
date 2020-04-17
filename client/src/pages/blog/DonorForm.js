import * as React from 'react';
import {render} from 'react-dom';
import {Formik, Form, Field} from 'formik';
import {
  Button,
  LinearProgress,
  MenuItem,
  FormControl,
  InputLabel,
} from '@material-ui/core';
import MuiTextField from '@material-ui/core/TextField';
import {
  fieldToTextField,
  TextField,
  TextFieldProps,
  Select,
} from 'formik-material-ui';
import * as Yup from 'yup';

const options = [
  {
    value: 'mask',
    label: 'mask',
  },
  {
    value: 'thermometer',
    label: 'thermometer',
  },
  {
    value: 'gloves',
    label: 'gloves (pairs)',
  },
  {
    value: 'sanitizer',
    label: 'sanitizer',
  },
  {
    value: 'toilet_paper',
    label: 'toilet paper',
  },
];

export default function DonorForm(){
  return (
  <Formik
    initialValues={{
      name: '',
      address: '',
      email: '',
      tel: '',
      select: 'mask',
      number: 1,
      tags: [],
      remark: '',
      dateTime: new Date(),
    }}
    validationSchema={Yup.object({
      name: Yup.string()
        .max(15, 'Must be 15 characters or less')
        .required('Required'),
      address: Yup.string()
        .required('Required'),
      email: Yup.string()
        .email('Invalid email address')
        .required('Required'),
      tel: Yup.string()
        .matches(/^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$/,'Invalid phone number')
        .required('Required'),
      number: Yup.number()
        .min(1, 'You must need at least 1')
        .required('Required'),
      jobType: Yup.string()
        .required('Required'),
    })}
    onSubmit={(values, {setSubmitting}) => {
      setTimeout(() => {
        setSubmitting(false);
        alert(JSON.stringify(values, null, 2));
      }, 500);
    }}
    render={({submitForm, isSubmitting, values, setFieldValue}) => (
      <Form>
        <Field component={TextField} type="name" label=" name" name="name" />
        <br />
        <br />
        <Field
          component={TextField}
          type="address"
          label=" your address"
          name="address"
        />
        <br />
        <br />
        <Field component={TextField} name="email" type="email" label="Email" />
        <br />
        <br />
        <Field component={TextField} name="tel" type="tel" label="tel" />
        <br />
        <br />
        <Field
          component={TextField}
          type="text"
          name="select"
          label="Resource Type"
          select
          variant="standard"
          helperText="Please select the type you want"
          margin="normal"
          InputLabelProps={{
            shrink: true,
          }}
        >
          {options.map(option => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </Field>
        <br />
        <Field
          component={TextField}
          type="number"
          label="number you need"
          name="number"
        />

        <br />
        <Field
          component={TextField}
          type="remark"
          label="remark"
          name="remark"
        />

        <br />
        {isSubmitting && <LinearProgress />}
        <br />

        <Button
          variant="contained"
          color="default"
          disabled={isSubmitting}
          onClick={submitForm}
        >
          Submit
        </Button>
      </Form>
    )}
  />
  );
};

