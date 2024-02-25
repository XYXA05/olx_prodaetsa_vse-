import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SersComponent } from './pages/sers/sers.component';
import { AnalizComponent } from './pages/analiz/analiz.component';
import { AnimatComponent } from './pages/animat/animat.component';

const routes: Routes = [
  {path:'main', component:SersComponent, pathMatch: 'full'},
  {path:'analiz', component:AnalizComponent, pathMatch:'full'},
  {path:'animat', component:AnimatComponent, pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
  
})
export class AppRoutingModule { }
