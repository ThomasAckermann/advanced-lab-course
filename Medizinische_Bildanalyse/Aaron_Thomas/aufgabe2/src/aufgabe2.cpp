// itk includes
#include "itkImageRegistrationMethodv4.h"
#include "itkMattesMutualInformationImageToImageMetricv4.h"
#include "itkMeanSquaresImageToImageMetricv4.h"
#include "itkEuler3DTransform.h"
#include "itkQuasiNewtonOptimizerv4.h"
#include "itkTimeProbe.h"

// function collection includes
#include "nrnGlobals.h"

// system includes
#include <sys/stat.h>
#include <fstream>
#include <stdlib.h>  
#include <iostream>
#include <iomanip>

int main( int argc, char *argv[] )
{
	const unsigned int dimension = 3;
	typedef  double PixelType;

	
   	unsigned int numberOfLevels = 3;
	unsigned int histBins = 0; //  URSPR�NGLICH 256
	std::vector<double> scale;
	std::vector<double> m1;
	std::vector<double> m2;

	for (unsigned i = 1; i <= 19; ++i)
	{
		double samplingPercentage = 0.9;
		// Laden der Daten:	
		typedef itk::Image< PixelType, dimension >  ImageType;
		ImageType::Pointer fixedImage = nrnLoadImage<ImageType>
			("C:/FP/Allgemein/Daten/training_001/ct/training_001_ct.mhd");
		ImageType::Pointer movingImage = nrnLoadImage<ImageType>("C:/FP/Allgemein/Daten/training_001/mr_T2/training_001_mr_T2.mhd");

		// Definition der Transformationen:
		typedef itk::Euler3DTransform<double> TransformType;
		TransformType::Pointer transform1 = TransformType::New();
		TransformType::Pointer transform2 = TransformType::New();

		// ideale Parameterkonfiguration
		// x_m = T * x_r
		TransformType::ParametersType optimalParameter;
		optimalParameter.SetSize(6);
		optimalParameter[0] = 0.004900056378026;
		optimalParameter[1] = -0.020648378633891;
		optimalParameter[2] = -0.077533129698997;
		optimalParameter[3] = 3.237299999999982;
		optimalParameter[4] = -33.884475000000000;
		optimalParameter[5] = -25.243600000000010;


		// 0-Konfiguration
		TransformType::ParametersType zeroParameter;
		zeroParameter.SetSize(6);
		zeroParameter[0] = 0;
		zeroParameter[1] = 0;
		zeroParameter[2] = 0;
		zeroParameter[3] = 0;
		zeroParameter[4] = 0;
		zeroParameter[5] = 0;

		transform1->SetParameters(optimalParameter);

		typedef itk::MattesMutualInformationImageToImageMetricv4<
			ImageType,
			ImageType >   MetricType;
		typedef itk::MeanSquaresImageToImageMetricv4<
			ImageType,
			ImageType >   MeanMetricType;


		MetricType::Pointer         metric = MetricType::New();
		MeanMetricType::Pointer     metric2 = MeanMetricType::New();

		metric->SetNumberOfHistogramBins(histBins);
		metric->SetFixedImage(fixedImage);
		metric->SetMovingImage(movingImage);
		metric->Initialize();

		metric2->SetFixedImage(fixedImage);
		metric2->SetMovingImage(movingImage);
		metric2->Initialize();
		// Transformieren des bewegten Bildes mit der idealen Transformation
		ImageType::Pointer resampledImage = resampleImage<ImageType, TransformType>
			(movingImage, fixedImage, transform1);
		// Speicherung des Ergebnisses
		nrnSaveImage<ImageType>("mr_optimal_transformed.mhd", resampledImage);

		// Vektoren zum Speichern der Metrikwerte




		histBins = histBins + 5;
		transform1->SetParameters(optimalParameter);
		metric->SetTransform(transform1);
		metric->GetValue();
		m1.push_back(metric->GetValue());
		metric2->SetTransform(transform1);
		metric2->GetValue();
		m2.push_back(metric2->GetValue());
		scale.push_back(histBins);




		//int max = 40;
		//double delta = 2;
		//optimalParameter[3] = optimalParameter[3] - max * delta / 2;
		//for (unsigned i = 1; i <= 41; ++i)
		//{
		//	transform1->SetParameters(optimalParameter);
		//	metric->SetTransform(transform1);
		//	metric->GetValue();
		//	m1.push_back(metric->GetValue());
		//	metric2->SetTransform(transform1);
		//	metric2->GetValue();
		//	m2.push_back(metric2->GetValue());
		//	scale.push_back(optimalParameter[3]);
		//	optimalParameter[3] = optimalParameter[3] + delta;
		//}

		// TODO: Ermittlung der Metrikwerte f�r verschiedene Parameterkonfigurationen
		//
		// Beispiele f�r die Arbeit mit Transformation und Metrik:
		// �ndern eines Parameters: 
		//       parameter[0] = Wert;
		// Danach Update der Parameter f�r eine Metrik: 
		//       transform1->SetParameters(parameter);
		//       metric->SetTransform(transform1);
		// Berechnung des Metrikwertes:
		//       metric->GetValue()
		// Speichern des Wertes in einem Vektor:
		//      m1.push_back(metric->GetValue());
		TransformType::ParametersType parameter = optimalParameter;

	}
	// Schreiben der Werte in eine Textdatei
	std::string out = "output.txt";
	std::ofstream outputfile;
	outputfile.open(out.c_str()/*, std::ofstream::app*/);


	for (unsigned int i=0; i< m1.size(); ++i)
	outputfile  << scale[i]	<<" "
				<< m1[i]	<< " "
				<< m2[i]	<<"\n";
	outputfile.close();
	return EXIT_SUCCESS;
}