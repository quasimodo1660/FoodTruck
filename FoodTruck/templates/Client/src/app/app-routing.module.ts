import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ShowComponent } from './show/show.component'
import { ShowapiComponent } from './showapi/showapi.component'
import { ReviewComponent } from './review/review.component'
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  { path: 'lunchbox/angular/:id', component:ShowComponent},
  
  // { path: 'getInfoFromAPI',component:ShowapiComponent},
  // { path: 'getAllReivew',component:ReviewComponent }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
