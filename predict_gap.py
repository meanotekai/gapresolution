from model3000x2x20482 import model 
import neuthink.metatext as Text 
model.LoadContent(Text.LoadColumn("diff_test.txt"))  #input file name here!
data2 = model.Unroll() 
d=data2.Text.Word2Chunk().model.Parent[0].Exec().DistributeFeatures(source='chunk',target='LSTM3').Child[0].BLSTM(source='LSTM3',target='ttg',size=256).dContextMap(size=256,target='term',source='ttg') 
d.enableGPU('cuda:1') 
model.enableGPU('cuda:1')   

data2.classes = ['cR1', 'cV', 'cR2', 'other', 'R1', 'R2', 'V']              
data2.LoadState('tempmodel.tmp')                                            
data2.Predict2(basemode="train")    #train mode for prediction is a hack, it works but is slow
Text.SaveColumn(model,"diff_test_result.txt",column_list=["word","pos_start","pos_end","dMap1"])    
