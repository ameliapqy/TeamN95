import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import GitHubIcon from '@material-ui/icons/GitHub';
import FacebookIcon from '@material-ui/icons/Facebook';
import TwitterIcon from '@material-ui/icons/Twitter';
import Header from './Header';
import MainFeaturedPost from './MainFeaturedPost';
import FeaturedPost from './FeaturedPost';
import Main from './Main';
import Sidebar from './Sidebar';
import Footer from './Footer';
import post1 from './blog-post.1.md';
import post2 from './blog-post.2.md';
import post3 from './blog-post.3.md';

import Paper from '@material-ui/core/Paper';
import DonorForm from './DonorForm';

const useStyles = makeStyles(theme => ({
  mainGrid: {
    marginTop: theme.spacing(3),
  },
  formPaper: {
    padding: theme.spacing(5),
  }
}));

const sections = [
  { title: 'Home', url: '../' },
  { title: 'Knowledge', url: '#' },
  { title: 'Donate Resources', url: '#' },
  { title: 'Seek Resources', url: '#' },
  { title: 'Data', url: 'https://github.com/datasets/covid-19' },
];

const mainFeaturedPost = {
  title: 'Let\'s\' work together in combatting Covid! ',
  description:
    "This is a website that facilitates exchange of medical resources in the time of medical emergencies such as the COVID-19 outbreak. Donors can input their resource information and seekers can input their requests, and this website would notify both parties when there is a possible match.",
  image: 'https://img.vixdata.io/pd/webp-large/pt/sites/default/files/c/coronavirus-covid-19-0320-1400x800-04.jpg',
  linkText: 'Start Donating...',
};

const featuredPosts = [
  {
    title: 'Latest US News about COVID',
    date: 'April 12',
    description:
      'Check out the latest news on COVID-19',
    image: 'https://cdn.vox-cdn.com/thumbor/MXqLyj3dLSB5SqIj8555YbE8-o8=/0x0:4000x2667/1820x1213/filters:focal(1680x1014:2320x1654):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66613362/1209296006.jpg.0.jpg',
    imageText: 'covid map',
    url: 'https://www.google.com/search?bih=766&biw=1440&hl=en&ei=sRqXXvjEJYXj9APg0KGgCg&q=covid+in+us&oq=covid+in+us&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABCDATIFCAAQgwEyBQgAEIMBMgIIADIFCAAQgwEyBQgAEIMBMgIIADIFCAAQgwE6BQghEKABOgUIABCRAjoECAAQQzoHCAAQgwEQQ0ovCBcSKzItMjU1ZzI2MGcyNTlnMjM0ZzIzOGcyMzlnMjMxZzI0NGcyMzdnMGczNDRKGwgYEhcyLTFnMWcxZzFnMWcxZzFnMWcxZzBnM1CRFVjoHGDZHmgBcAB4AYAB1QOIAaYbkgEIMi0xMS4xLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi44cLY0uroAhWFMX0KHWBoCKQQ4dUDCAw&uact=5',
  },
  {
    title: 'How is the world responding to COVID-19?',
    date: 'April 12',
    description:
      'This is a wider card with supporting text below as a natural lead-in to additional content.',
    image: 'https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2020/3/15/747c29da2b1a484d8c5fc426f4688552_18.jpg',
    imageText: 'spain covid',
    url: 'https://www.google.com/search?bih=766&biw=1440&hl=en&ei=thqXXuaVGqes0PEP9ZWDsAc&q=covid+in+the+world&oq=covid+in+the+world&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABDNAjIFCAAQzQIyBQgAEM0CMgUIABDNAjoECAAQRzoCCABKEQgXEg05LTI2MWcxMzBnMjQ5SgwIGBIIOS0xZzEyZzJQsMIBWI3LAWChzAFoAHAGeACAAaACiAHEEZIBAzItOZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjmyOja0uroAhUnFjQIHfXKAHYQ4dUDCAw&uact=5',
  },
];

const posts = [post1, post2, post3];

const sidebar = {
  title: 'About',
  description: 'Made by: Yiwei (Estee) Chen, Qingyuan (Amelia) Peng, Audrey Zheng',
  archives: [
    { title: 'FemmeHacks 2020 Best Hack for Social Impact', url: 'https://devpost.com/software/medunicorn' },
    { title: 'Github Resource', url: 'https://github.com/qingyuanpeng/TeamN95' },
  ],
  social: [
    { name: 'GitHub', icon: GitHubIcon },
    { name: 'Twitter', icon: TwitterIcon },
    { name: 'Facebook', icon: FacebookIcon },
  ],
};

export default function Blog() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <Header title="TeamN95: Emergency Medical Resource Locator" sections={sections} />
        <main>
          <MainFeaturedPost post={mainFeaturedPost} />
          <Grid container spacing={4} id="formPosition">
            <Grid item xs={12} md={6} lg={6}>  
              <Paper className={classes.formPaper}> 
                <h3> Donors: fill in your information here!</h3>
                <DonorForm />
                
              </Paper>
            </Grid>
            <Grid item xs={12} md={6} lg={6}>  
              <Paper className={classes.formPaper}> 
                <h3> Seekers: fill in your information here!</h3>
                <DonorForm />
                
              </Paper>
            </Grid>
            {featuredPosts.map(post => (
              <FeaturedPost key={post.title} post={post} />
            ))}
          </Grid>
          <Grid container spacing={5} className={classes.mainGrid}>
            <Main title="Where are the resources? Google Map placed here" />
            <Sidebar
              title={sidebar.title}
              description={sidebar.description}
              archives={sidebar.archives}
              social={sidebar.social}
            />
          </Grid>
        </main>
      </Container>
      <Footer title="Team N95" description="Join us in making the world a better place!" />
    </React.Fragment>
  );
}
