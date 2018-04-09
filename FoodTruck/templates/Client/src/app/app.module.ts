import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { ShowComponent } from './show/show.component';
import { ChatboxComponent } from './chatbox/chatbox.component';
import { ShowmapComponent } from './showmap/showmap.component';
import { ShowinfoComponent } from './showinfo/showinfo.component';
import { NaviCoComponent } from './navi-co/navi-co.component';
import { ReviewComponent } from './review/review.component';
import { ShowapiComponent } from './showapi/showapi.component';

import { HttpService } from './http.service';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientJsonpModule } from '@angular/common/http';

import { NgxGalleryModule } from 'ngx-gallery';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AgmCoreModule } from '@agm/core';
import { ProfileComponent } from './profile/profile.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ShareModule } from '@ngx-share/core';
import { ShareButtonModule } from '@ngx-share/button';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { ShareButtonsModule } from '@ngx-share/buttons';





@NgModule({
  declarations: [
    AppComponent,
    ShowComponent,
    ChatboxComponent,
    ShowmapComponent,
    ShowinfoComponent,
    NaviCoComponent,
    ReviewComponent,
    ShowapiComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgxGalleryModule,
    NgbModule.forRoot(),
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyAD1BgNBjRye5nHsUPtz-EukHsXe4anQhc'
    }),
    HttpClientJsonpModule,  // for linkedin and tumblr share counts
    // ShareModule.forRoot(),
    ShareButtonModule.forRoot(), 
    AngularFontAwesomeModule,
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
